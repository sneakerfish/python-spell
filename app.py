import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine

import get_ngrams
import find_word

sql_user = os.environ['SQL_USER']
sql_pass = os.environ['SQL_PASS']
sql_db   = os.environ['SQL_DB']
sql_host = os.environ['SQL_HOST']
engine = create_engine("postgresql+psycopg2://{}:{}@{}/{}".
                     format(sql_user, sql_pass, sql_host, sql_db))

conn = engine.connect()
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/check', methods=['GET'])
def check_word():
    if 'word' in request.args:
        word = request.args['word']
        return jsonify(find_word.find_word(conn, word))

@app.route('/ngrams', methods=['GET'])
def decompose_ngrams():
    if 'word' in request.args:
        word = request.args['word']
        return jsonify(get_ngrams.get_ngrams(word))

@app.route('/lev', methods=['GET'])
def levenshtein_distance():
    if 'worda' in request.args and 'wordb' in request.args:
        return jsonify(find_word.levenshtein(conn, request.args['worda'], request.args['wordb']))

if __name__ == '__main__':
    app.run(debug=True)
