"""Task 2 tests: turning a value into a flag."""

from lab_checker.checker import parse_value, classify


# ---- parse_value ----

def test_parse_normal_number():
    assert parse_value("11.2") == 11.2


def test_parse_whole_number():
    assert parse_value("260") == 260.0


def test_parse_strips_spaces():
    assert parse_value("  88 ") == 88.0


def test_parse_empty_is_none():
    assert parse_value("") is None


def test_parse_text_is_none():
    assert parse_value("N/A") is None


def test_parse_none_is_none():
    assert parse_value(None) is None


# ---- classify ----

def test_low():
    assert classify(11.2, 12.0, 15.5) == "LOW"


def test_normal():
    assert classify(13.0, 12.0, 15.5) == "NORMAL"


def test_high():
    assert classify(5.6, 0.4, 4.0) == "HIGH"


def test_exactly_low_limit_is_normal():
    assert classify(12.0, 12.0, 15.5) == "NORMAL"


def test_exactly_high_limit_is_normal():
    assert classify(11.0, 4.0, 11.0) == "NORMAL"


def test_critical_low():
    assert classify(6.4, 12.0, 15.5, critical_low=7.0, critical_high=20.0) == "CRITICAL_LOW"


def test_critical_high():
    assert classify(6.9, 3.5, 5.1, critical_low=2.5, critical_high=6.5) == "CRITICAL_HIGH"


def test_low_but_not_critical():
    assert classify(3.4, 3.5, 5.1, critical_low=2.5, critical_high=6.5) == "LOW"


def test_no_critical_limits_given():
    assert classify(10.0, 0.4, 4.0) == "HIGH"
