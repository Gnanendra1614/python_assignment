from src.word_order.util import word_order


def test_word_order():
    words = ["bcdef", "abcdefg", "bcde", "bcdef"]

    result = word_order(words)

    assert result == (3, [2, 1, 1])