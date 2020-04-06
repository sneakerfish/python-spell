import os
from sqlalchemy import create_engine, func
from sqlalchemy.sql import select, and_
from tables import ngrams, words
import get_ngrams

def levenshtein(conn, worda, wordb):
    """Return the Levenshtein Distance between worda and wordb.
    Levenshtein distance measures the number of edits to get from one
    string to another string.  Since we're going to the database
    anyway and since we're counting on this function in the database
    for sorting, we might as well use that function to provide the
    result.
    """
    lev = func.levenshtein(worda, wordb)
    s = select([lev])
    result = conn.execute(s)
    return [row[0] for row in result]


def find_word(conn, word, limit_to=10):
    """Find the word in the dictionary and find related words if it is not
    found. This involves a call to the database searching for words
    with common n-grams and then sorting the results by closeness to
    the original word (the levenshtein distance).
    """
    word_grams = get_ngrams.get_ngrams(word)
    lev = func.levenshtein(words.c.spelling, word)
    s = select([words, lev]).where(and_(ngrams.c.word_id == words.c.id,
                                        ngrams.c.ngram.in_(word_grams))).distinct().limit(limit_to).order_by(lev)
    result = conn.execute(s)
    return [(row[1], row[2]) for row in result]

