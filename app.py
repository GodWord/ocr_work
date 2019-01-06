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
        path = BASE_DIR + "/media/"

        img_path = os.path.join(path, 'photo', image.filename)
        txt_path = os.path.join(path, 'txt', image.filename.split('.')[0] + '.txt')
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.exists(img_path):
            os.remove(img_path)
        image.save(img_path)

        options = OCR_CONFIG['OPTIONS']
        utils = OCRUtils()
        data = utils.ocr(utils.get_file_content(img_path), options)

        words = reduce(lambda x, y: x + '\n' + y, map(lambda x: x['words'], data['words_result']))
        utils.save_res(words, txt_path)
        filename = image.filename

        data['filename'] = filename
        return Response(json.dumps(data), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8055)
