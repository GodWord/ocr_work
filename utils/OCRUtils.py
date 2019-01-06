# -*- coding:utf-8 -*-

from aip import AipOcr

from setting.setting import OCR_CONFIG


class OCRUtils:
    def __init__(self):
        self.client = AipOcr(OCR_CONFIG['APP_ID'], OCR_CONFIG['API_KEY'], OCR_CONFIG['SECRET_KEY'])

    def ocr(self, image: bytes, options=None):
        return self.client.basicGeneral(image, options)

    @staticmethod
    def get_file_content(file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()
