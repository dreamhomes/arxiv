from datetime import datetime

import fire
from dateutil.parser import parse

from crawler.data.paper import translate_paper
from crawler.data.topic import Topic
from crawler.format_md import format_markdown
from crawler.parse_data import parse_feed
from crawler.request_data import request_api

root_dir = "papers/"


def main(topic: str, date: str = None, to_translate: bool = False, gap:int = 1):
    """
    Search Arxiv papers according to date and keywords.
    :param to_translate: translate abstract or not
    :param topic: "graph", "time series"
    :param date: "2022-3-9"
    :return:
    """
    topic = Topic(topic)
    output_dir = root_dir + topic.value.replace(' ', '-')
    date = datetime.now() if date is None else parse(date)
    md_file_name = date.strftime("%Y-%m-%d")
    max_results = 50
    max_num_papers = 10

    # 1. Get data.
    xml = request_api(topic.value, max_results)
    # 2. Parse data.
    papers = parse_feed(xml, date, gap)[:max_num_papers]

    if len(papers) == 0:
        return
    # 3. Translate abstract
    if to_translate:
        papers = list(map(translate_paper, papers))
    # 4. Format markdown.
    format_markdown(topic, papers, output_dir, md_file_name)


if __name__ == "__main__":
    # main(Topic.TS.value)
    # main(Topic.GRAPH.value)
    fire.Fire(main)
