
import json
import os
import importlib
from flask import Flask, request,jsonify
import requests
# from InsertIntoDB import insertIntoDB


app = Flask(__name__)


@app.route("/")
def start():
    from stanfordcorenlp import StanfordCoreNLP
    with StanfordCoreNLP(r'E:/stanford-corenlp-full-2018-10-05/stanford-corenlp-full-2018-10-05', lang='zh',memory='4g', quiet=True) as nlp:
        return nlp

if __name__ == '__main__':
    app.run(debug=True, port=8081)