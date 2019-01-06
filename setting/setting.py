# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/1/4 11:09'

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OCR_CONFIG = {
    'APP_ID': '15191630',
    'API_KEY': '6N3ZkEujGxlGGU2sOhM1CZug',
    'SECRET_KEY': 'EkctmyzWn2MOw6o1HbBVosxRINUYsTtm',
    'OPTIONS': {
        'language_type': 'CHN_ENG',
        '+words': 'true'
    }
}

OCR_API = {
    'baidu': {
        'ocr_url': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
        'token_url': 'https://aip.baidubce.com/oauth/2.0/token',
        'data': {
            'appid': 15191630,
            'client_id': '6N3ZkEujGxlGGU2sOhM1CZug',
            'client_secret': 'EkctmyzWn2MOw6o1HbBVosxRINUYsTtm',
            'grant_type': 'client_credentials'
        },

    }
}
