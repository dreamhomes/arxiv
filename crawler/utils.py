# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/8
@Author      : shenmengjia
@File        : utils.py
@Description : utilities
"""
import hashlib
import random
from time import sleep

import requests
import configparser


def get_translate_config(config_path: str):
    parser = configparser.ConfigParser()
    parser.read(config_path)
    assert "TRANSLATE" in parser.sections(), "Error in config file."
    return parser["TRANSLATE"]


config = get_translate_config("config/config.ini")
APP_ID = config["APP_ID"]
SECRET_KEY = config["SECRET_KEY"]
API_URL = config["API_URL"]
MAX_TIME = config.getint("MAX_TIME")


def translate(english_str: str) -> str:
    salt = str(random.randint(32768, 65536))
    pre_sign = APP_ID + english_str + salt + SECRET_KEY
    sign = hashlib.md5(pre_sign.encode()).hexdigest()
    result = None
    times = 0
    params = {
        "q": english_str,
        "from": "auto",
        "to": "zh",
        "appid": APP_ID,
        "salt": salt,
        "sign": sign,
    }
    while result is None and times < MAX_TIME:
        times += 1
        result = requests.get(API_URL, params=params).json().get("trans_result")
        print(f"Translate errors [{times}], Retry...")
        sleep(1)
    chinese_str = result[0].get("dst").replace('\n', '').replace('\r', '').replace(' ', '')
    return chinese_str if result is not None else english_str
