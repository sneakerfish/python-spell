
from ngrams import ngrams

class TestNGrams:
    def test_a(self):
        assert ngrams("a") == ["*a*"]
    def test_ab(self):
        assert ngrams("ab") == ["*ab", "ab*"]
    def test_abc(sefl):
        assert ngrams("abc") == ["*ab", "abc", "bc*"]
