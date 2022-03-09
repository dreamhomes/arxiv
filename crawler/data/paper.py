from dataclasses import dataclass, field
from datetime import datetime

from crawler.utils import translate


@dataclass
class Paper:
    id: str
    link: str
    title: str
    published: datetime
    authors: list[str]
    abstract: str
    comment: str
    abstract_zh: str = field(hash=False, compare=False, default=None)


def translate_paper(paper: Paper):
    paper.abstract_zh = translate(paper.abstract)
    return paper
