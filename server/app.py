'''
Flask tutorial:
    https://www.maxlist.xyz/2020/05/01/flask-list/?fbclid=IwAR1kJ8_izhNQWDzHx6YWtrM4RrfbSpxq2h81ERSGQo24lx2kPA_3eURkc70
'''
import sys
from flask import Flask, request, render_template
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


@app.route('/', methods=['POST'])
def result():
    document = request.form['text']
    result = document_extractor.run(document)
    return render_template('page.html', length=len(result), result=result)


@app.route('/')
def main_page():
    return render_template('page.html', length=0, result=[])

if __name__ == '__main__':
    # initialize the document extraction
    document_extractor = BertDocumentExtractor()

    # run server
    app.run(debug=True)
