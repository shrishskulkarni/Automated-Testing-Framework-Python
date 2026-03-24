"""
test_cases.py
-------------
Contains individual test functions for the automated testing framework.

Each function uses assertions. Two tests intentionally pass, and one
test intentionally fails to demonstrate failure handling.
"""


def test_addition() -> None:
    """Pass test: verifies basic addition."""
    assert 2 + 3 == 5, "Addition test failed: 2 + 3 should be 5."


def test_string_uppercase() -> None:
    """Pass test: verifies string upper conversion."""
    assert "automation".upper() == "AUTOMATION", (
        "Uppercase test failed: expected 'AUTOMATION'."
    )


def test_intentional_failure() -> None:
    """Fail test: intentionally wrong expected value."""
    assert 10 * 2 == 25, "Intentional failure: 10 * 2 is not 25."


def get_test_cases():
    """
    Return all test functions in a list.

    Keeping this in one place makes it easy to add/remove tests later.
    """
    return [
        test_addition,
        test_string_uppercase,
        test_intentional_failure,
    ]
