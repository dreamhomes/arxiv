# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/9
@Author      : shenmengjia
@File        : test_topic.py
@Description : 
"""
from crawler.data.topic import Topic


def test_to_zh():
    print(type(Topic("time series")))
    assert Topic("time series") == Topic.TS, "转义错误"
    assert Topic.GRAPH.value == "graph", "转义错误"
    assert Topic.to_zh(Topic.GRAPH) == "图机器学习", "转义错误"
