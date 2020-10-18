'''
Flask tutorial:
    https://www.maxlist.xyz/2020/05/01/flask-list/?fbclid=IwAR1kJ8_izhNQWDzHx6YWtrM4RrfbSpxq2h81ERSGQo24lx2kPA_3eURkc70
'''
from flask import Flask
from flask import request
from src.document_extractor import BertDocumentExtractor

app = Flask(__name__)


def _shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown')
def shutdown():
    _shutdown_server()
    return 'Server shutting down...'


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # initialize the document extraction
    #document_extractor = BertDocumentExtractor()

    # run server
    app.run()
