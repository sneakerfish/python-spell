
import os
from sqlalchemy import create_engine, MetaData, Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import tables
import get_ngrams
import find_word

Base = declarative_base()
global engine

engine = None

class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True)
    spelling = Column(String(255))

class NGram(Base):
    __tablename__ = "ngrams"
    id = Column(Integer, primary_key=True)
    ngram = Column(String(3))
    word_id = Column(Integer, ForeignKey('words.id'))

def load_data_file(engine, filename):
    all_words = []
    with open(filename, "r") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            word = line.strip().lower()
            all_words.append(word)
            line = fp.readline()
            cnt += 1
    session = Session(bind=engine)
    session.bulk_save_objects(
        [Word(spelling=word) for word in all_words]
        )
    session.commit()
    all_ngrams = []
    for word in session.query(Word):
        ngrams = get_ngrams.get_ngrams(word.spelling)
        all_ngrams += [NGram(ngram=ng, word_id=word.id) for ng in ngrams]
    session.bulk_save_objects(all_ngrams)
    session.commit()

if __name__ == "__main__":
    sql_user = os.environ['SQL_USER']
    sql_pass = os.environ['SQL_PASS']
    sql_db   = os.environ['SQL_DB']
    sql_host = os.environ['SQL_HOST']
    engine = create_engine("postgresql+psycopg2://{}:{}@{}/{}".
                           format(sql_user, sql_pass, sql_host, sql_db))
    filename = "tiny_sample_dictionary.txt"

    metadata = MetaData()
    Base.metadata.drop_all(engine)
    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    load_data_file(engine, filename)
