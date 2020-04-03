
def get_ngrams(word, n=3, add_stop_char='*'):
    word_to_decompose = word
    if add_stop_char:
        word_to_decompose = add_stop_char + word_to_decompose + add_stop_char
    return [word_to_decompose[i:i+n] for i in range(len(word_to_decompose)-(n-1))]
