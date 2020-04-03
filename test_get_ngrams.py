
from get_ngrams import get_ngrams

class TestNGrams:
    def test_a(self):
        assert get_ngrams("a") == ["*a*"]
    def test_ab(self):
        assert get_ngrams("ab") == ["*ab", "ab*"]
    def test_abc(sefl):
        assert get_ngrams("abc") == ["*ab", "abc", "bc*"]
