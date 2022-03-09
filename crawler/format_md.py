# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/8
@Author      : shenmengjia
@File        : format_md.py
@Description : https://github.com/didix21/mdutils
"""
from pathlib import Path

from mdutils.mdutils import MdUtils

from crawler.data.paper import Paper
from crawler.data.topic import Topic


def format_markdown(topic: Topic, papers: list[Paper], output_dir: str, file_name: str):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    file_name = (output_dir / f"{file_name}.md").as_posix()
    md_file = MdUtils(file_name=file_name, title=f"[{Topic.to_zh(topic)}] 每日论文速递", author="dreamhomes")
    for idx, paper in enumerate(papers):
        print(f"{idx + 1:<3} {paper}")
        md_file.new_header(level=3, title=str(idx + 1), add_table_of_contents="n")
        write_paper(md_file, paper)

    md_file.create_md_file()


def write_paper(md_file: MdUtils, paper: Paper):
    md_file.new_line("论文标题", bold_italics_code="b") + md_file.write(
        " "
    ) + md_file.write(paper.title, bold_italics_code="i")
    md_file.new_line("论文作者", bold_italics_code="b") + md_file.write(
        " "
    ) + md_file.write(",".join(paper.authors), bold_italics_code="i")
    md_file.new_line("发表时间", bold_italics_code="b") + md_file.write(
        " "
    ) + md_file.write(paper.published.strftime("%Y-%m-%d"), bold_italics_code="i")
    md_file.new_line("论文摘要", bold_italics_code="b") + md_file.write(
        " "
    ) + md_file.write(
        paper.abstract_zh if paper.abstract_zh is not None else paper.abstract,
        bold_italics_code="i",
    )
    md_file.new_line("论文链接", bold_italics_code="b") + md_file.write(
        " "
    ) + md_file.write(paper.link, bold_italics_code="i")
    if paper.comment is not None:
        md_file.new_line("论文批注", bold_italics_code="b") + md_file.write(
            " "
        ) + md_file.write(paper.comment, bold_italics_code="i")
