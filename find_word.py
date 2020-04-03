import os
from sqlalchemy import create_engine, func
from sqlalchemy.sql import select, and_
from tables import ngrams, words
import get_ngrams

sql_user = os.environ['SQL_USER']
sql_pass = os.environ['SQL_PASS']
sql_db   = os.environ['SQL_DB']
sql_host = os.environ['SQL_HOST']
engine = create_engine("postgresql+psycopg2://{}:{}@{}/{}".
                     format(sql_user, sql_pass, sql_host, sql_db))

conn = engine.connect()

word = "exactlally"


def find_word(conn, word, limit_to=10):
    word_grams = get_ngrams.get_ngrams(word)
    lev = func.levenshtein(words.c.spelling, word)
    s = select([words, lev]).where(and_(ngrams.c.word_id == words.c.id,
                                        ngrams.c.ngram.in_(word_grams))).distinct().limit(limit_to).order_by(lev)
    result = conn.execute(s)
    return [(row[1], row[2]) for row in result]
