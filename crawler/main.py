from crawler.data.paper import Paper, translate_paper
from crawler.data.topic import Topic
from crawler.request_data import request_api
from crawler.parse_data import parse_feed
from crawler.format_md import format_markdown

from datetime import datetime
from dateutil.parser import parse

root_dir = "papers/"


def main(topic: str, date: str = None, to_translate: bool = False):
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
    papers = parse_feed(xml, date)[:max_num_papers]
    # 3. Translate abstract
    if to_translate:
        papers = list(map(translate_paper, papers))
    # 4. Format markdown.
    format_markdown(topic, papers, output_dir, md_file_name)


if __name__ == '__main__':
    date = "2022-03-08"
    main(Topic.TS.value, date)
    main(Topic.GRAPH.value, date)
