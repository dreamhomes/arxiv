# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/9
@Author      : shenmengjia
@File        : topic.py
@Description : paper topic
"""

from enum import Enum, unique


@unique
class Topic(Enum):
    TS = "time series"
    GRAPH = "graph"

    @classmethod
    def to_zh(cls, key) -> str:
        en_zh_map = {
            cls.TS: "时间序列",
            cls.GRAPH: "图机器学习"
        }
        return en_zh_map.get(key)
