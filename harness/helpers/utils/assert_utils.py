from typing import Any


class Assertion:
    """Custom assertion.

    To have the compared failed items be always printed in the message of pytest test,
    when assertion is not on test level but in verifier classes.
    """

    def __init__(self, message: str = "\nAR:\n\t{0}\nER:\n\t{1}"):
        self._message = message

    def equal(self, actual: Any, expected: Any) -> None:
        assert actual == expected, self._message.format(actual, expected)

    def greater_or_equal(self, actual: Any, expected: Any) -> None:
        assert actual >= expected, self._message.format(actual, expected)

    def not_equal(self, actual: Any, expected: Any) -> None:
        assert actual != expected, self._message.format(actual, expected)

    def true(self, value: bool) -> None:
        assert value, self._message.format(value, True)

    def false(self, value: bool) -> None:
        assert not value, self._message.format(value, False)

    def in_list(self, actual: Any, expected: list[Any]) -> None:
        assert actual in expected, self._message.format(actual, expected)

    def not_in_list(self, actual: Any, expected: list[Any]) -> None:
        assert actual not in expected, self._message.format(actual, expected)


assertion = Assertion()
