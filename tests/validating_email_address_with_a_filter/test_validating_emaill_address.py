from src.validating_email.util import fun, filter_mail


def test_valid_email():
    assert fun("brian-23@hackerrank.com") is True


def test_invalid_email():
    assert fun("lara@hackerrank") is False


def test_filter_mail():
    emails = [
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com",
        "lara@hackerrank.com",
        "invalid@email.toolong"
    ]

    assert filter_mail(emails) == [
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com",
        "lara@hackerrank.com"
    ]