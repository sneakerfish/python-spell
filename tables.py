
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

words = Table('words', metadata,
              Column('id', Integer, primary_key=True),
              Column('spelling', String)
              )

ngrams = Table('ngrams', metadata,
               Column('id', Integer, primary_key=True),
               Column('ngram', String),
               Column('word_id', None, ForeignKey('words.id'))
               )
