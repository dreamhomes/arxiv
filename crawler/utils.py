# -*- coding: utf-8 -*-

"""
@Time        : 2022/3/8
@Author      : shenmengjia
@File        : utils.py
@Description : utilities
"""
import random
import hashlib
from time import sleep

import requests

APP_ID = "20220308001116256"
SECRET_KEY = "xFBa2W24XI6xXkrLcEmL"
apiURL = "http://api.fanyi.baidu.com/api/trans/vip/translate"
MAX_TIME = 5


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
        result = requests.get(apiURL, params=params).json().get("trans_result")
        print(f"Translate errors [{times}], Retry...")
        sleep(1)
    return result[0].get("dst").replace('\n', '').replace('\r', '') if result is not None else english_str
