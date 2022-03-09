# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/8
@Author      : shenmengjia
@File        : request_data.py
@Description : https://arxiv.org/help/api/user-manual
"""
from urllib import request
from urllib import parse

api_url = "http://export.arxiv.org/api/query?" \
          "search_query=ti:{0}+AND+abs:{0}" \
          "&start=0&max_results={1}" \
          "&sortBy=submittedDate" \
          "&sortOrder=descending"


# sortBy can be "relevance", "lastUpdatedDate", "submittedDate"
# sortOrder can be either "ascending" or "descending"

def request_api(keywords: str, max_results: int) -> str:
    url = api_url.format(parse.quote(keywords), max_results)
    print(f"Search url: {url}")
    data = request.urlopen(url).read()
    return data
