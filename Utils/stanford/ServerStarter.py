
from flask import Flask
import urllib.request


app = Flask(__name__)


@app.route("/start")
def start():
    from stanfordcorenlp import StanfordCoreNLP
    nlp = StanfordCoreNLP(r'E:/stanford-corenlp-full-2018-10-05/stanford-corenlp-full-2018-10-05', lang='zh',memory='4g', quiet=True):
    global nlp

@app.route("/server")
def server():
    return nlp

if __name__ == '__main__':
    app.run(debug=True, port=8081)
    urllib.request.urlopen('http://127.0.0.1:8081/start')