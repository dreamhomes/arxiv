# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/8
@Author      : shenmengjia
@File        : parse_data.py
@Description : https://pythonhosted.org/feedparser/common-atom-elements.html#accessing-common-entry-elements
"""
import pytz

from datetime import datetime, timedelta
from multiprocessing import Pool, cpu_count

import feedparser as parser
from dateutil.parser import parse

from crawler.data.paper import Paper


def parse_feed(xml_str: str, date: datetime) -> list[Paper]:
    entries = parser.parse(xml_str).get("entries")
    with Pool(cpu_count()) as pool:
        papers = pool.map(parse_paper, entries)
    utc_date = date.replace(tzinfo=pytz.timezone('UTC'))
    lower_bound = (date - timedelta(days=1)).replace(tzinfo=pytz.timezone('UTC'))
    filtered_papers = filter(lambda paper: lower_bound <= paper.published <= utc_date, papers)

    return list(filtered_papers)


def parse_paper(entry: dict) -> Paper:
    paper_id = entry.get("id")
    link = entry.get("link")
    published = parse(entry.get("published"))
    title = entry.get("title")
    summary = entry.get("summary").replace('\n', '').replace('\r', '')
    authors = [author.get("name") for author in entry.get("authors")]
    comment = entry.get("arxiv_comment")

    return Paper(paper_id, link, title, published, authors, summary, comment)
