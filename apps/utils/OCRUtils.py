# -*- coding:utf-8 -*-
import base64
import json
from urllib.parse import urlencode

import requests

from setting.setting import OCR_API


class OCRUtils:
    @staticmethod
    def get_token():
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        params = OCR_API['baidu']['data']
        del params['appid']
        req = requests.get(OCR_API['baidu']['token_url'], params=params, headers=headers)
        data = json.loads(req.content)
        return data

    @staticmethod
    def post_api():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        with open('test.png', 'rb') as file:
            base64_data = base64.b64encode(file.read())
        data = {
            'access_token': OCRUtils.get_token()['access_token'],
            'image': base64_data,
            'detect_direction': True,
            'detect_language': True,
        }
        req = requests.post(OCR_API['baidu']['ocr_url'], headers=headers, data=data)
        res = json.loads(req.content)
        return res

    @staticmethod
    def api(img):
        OCRUtils.post_api()


if __name__ == '__main__':
    res = OCRUtils().post_api()
    for words in res['words_result']:
        print(words['words'].encode('utf-8'))
