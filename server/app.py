'''
Flask tutorial:
    https://www.maxlist.xyz/2020/05/01/flask-list/?fbclid=IwAR1kJ8_izhNQWDzHx6YWtrM4RrfbSpxq2h81ERSGQo24lx2kPA_3eURkc70
Flask CORS:
    https://medium.com/@charming_rust_oyster_221/flask-%E5%AF%A6%E7%8F%BE-cors-%E8%B7%A8%E5%9F%9F%E8%AB%8B%E6%B1%82%E7%9A%84%E6%96%B9%E6%B3%95-c51b6e49a8b5
Leveraging BERT for Extractive Text Summarization on Lectures:
    https://arxiv.org/abs/1906.04165
BERT abstractive summarization:
    1. pretrain with gap sentence generation (original one for bert is sentence matching classification)
    2. mask language model
    3. train the pretrained model with lots of article with summarization
    https://arxiv.org/pdf/1912.08777.pdf
'''
import sys
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from src.document_extractor import BertDocumentExtractor
from service.service import Service
from googletrans import Translator

app = Flask(__name__)
CORS(app)


def _shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown')
def shutdown():
    _shutdown_server()
    return 'Server shutting down...'


@app.route('/inference', methods=['POST'])
def result():
    try:
        result = Service(request, document_extractor, translator)
        return jsonify(result)
    except Exception as e:
        return jsonify({"english_result": "Error: {}".format(e), "chinese_result": "錯誤: {}".format(e)})


@app.route('/', methods=['POST'])
def main():
    return render_template('page.html')


@app.route('/')
def main_page():
    return render_template('page.html', length=0, result=[])


if __name__ == '__main__':
    # initialize the document extractor and translator
    document_extractor = BertDocumentExtractor()
    translator = Translator()

    # run server
    app.run(debug=True)
