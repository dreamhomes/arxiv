# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/8
@Author      : shenmengjia
@File        : test_utils.py
@Description : test
"""

from crawler.utils import translate


def test_translate():
    assert translate("chinese") == "中国人", "翻译错误"
