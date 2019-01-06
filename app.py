import json
import os
from functools import reduce

from flask import Flask, request, render_template, redirect, url_for, Response

from utils.OCRUtils import OCRUtils
from setting.setting import OCR_CONFIG, BASE_DIR

app = Flask(__name__)
app.debug = True


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        image = request.files.get('file')
        path = BASE_DIR + "/media/photo/"
        file_path = path + image.filename
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.exists(file_path):
            os.remove(file_path)
        image.save(file_path)

        options = OCR_CONFIG['OPTIONS']
        utils = OCRUtils()
        data = utils.ocr(utils.get_file_content(file_path), options)
        words = reduce(lambda x, y: x + '<br>' + y, map(lambda x: x['words'], data['words_result']))
        filename = image.filename
        # res = {
        #     'filename': filename,
        #     'words': data['words']
        # }
        data['filename'] = filename
        return Response(json.dumps(data), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
