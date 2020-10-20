'''
Flask tutorial:
    https://www.maxlist.xyz/2020/05/01/flask-list/?fbclid=IwAR1kJ8_izhNQWDzHx6YWtrM4RrfbSpxq2h81ERSGQo24lx2kPA_3eURkc70
Flask CORS:
    https://medium.com/@charming_rust_oyster_221/flask-%E5%AF%A6%E7%8F%BE-cors-%E8%B7%A8%E5%9F%9F%E8%AB%8B%E6%B1%82%E7%9A%84%E6%96%B9%E6%B3%95-c51b6e49a8b5
'''
import sys
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from src.document_extractor import BertDocumentExtractor

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
    document = request.get_json()['params']['document']
    result = document_extractor.run(document)
    
    # test loading icon
    import time
    time.sleep(3)

    return jsonify({"result": result})


@app.route('/', methods=['POST'])
def main():
    return render_template('page.html')


@app.route('/')
def main_page():
    return render_template('page.html', length=0, result=[])

if __name__ == '__main__':
    # initialize the document extraction
    document_extractor = BertDocumentExtractor()

    # run server
    app.run(debug=True)
