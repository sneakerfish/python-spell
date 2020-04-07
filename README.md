# python-spell

A serverless web app to check spelling and suggest alternate words.

Spell checking is based on two algorithms, n-gram Decomposition and
Levenshtein Distance.  N-gram decomposition is the process of breaking
apart a string into each proper n-letter substring (with two extra
ones added for the beginning and ending of the word). Levenshtein
distance is the measurement of the distance in edits between two
strings.

## API
  * /check?word=MISSPELLEDWORD
  * /ngrams?word=WORD
  * /levenshtein?a=WORD1&b=WORD2

## Code:

  * [app.py] -- Flask app for API
  * [find_word.py] -- Use the database to find similar words
  * [get_ngrams.py] -- Decompose words into n-grams
  * [tables.py] -- SQLAlchemy table definitions
  * [test_get_ngrams.py] -- PyTest test cases for get_ngrams.py.
