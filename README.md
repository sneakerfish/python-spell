# python-spell

A serverless web app to check spelling and suggest alternate words.

Spell checking is based on two algorithms, n-gram Decomposition and
Levenshtein Distance.  N-gram decomposition is the process of breaking
apart a string into each proper n-letter substring (with two extra
ones added for the beginning and ending of the word). Levenshtein
distance is the measurement of the distance in edits between two
strings.

The database can be seeded using the program `seed_database.py`.  You
will need a file where the words are listed one-per-line like in the
sample dictionary provided in this repo.  I usually use the one at
https://github.com/dwyl/english-words.

## API
  * /check?word=MISSPELLEDWORD
  * /ngrams?word=WORD
  * /levenshtein?a=WORD1&b=WORD2

## Code:

  * [app.py] -- Flask app for API
  * [find_word.py] -- Use the database to find similar words
  * [get_ngrams.py] -- Decompose words into n-grams
  * [seed_database.py] -- Seed the database from a word list file
  * [tables.py] -- SQLAlchemy table definitions
  * [test_get_ngrams.py] -- PyTest test cases for get_ngrams.py
  * [tiny_sample_database.txt] -- A really short word list for testing
