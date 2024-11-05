from collections.abc import Callable
from time import sleep
from time import time
from typing import Any

from harness.config.logger import Logger


class _Retry:
    def __init__(
        self,
        duration: int = 5,
        interval_timeout: float = 0.5,
        exceptions: tuple = (Exception,),
        raise_error_on_failure: bool = True,
        error_on_failure: Exception | None = None,
    ):
        """Decorator to retry actions

        :param exceptions: a tuple of exceptions to catch. All exceptions by default.
        :param raise_error_on_failure: bool flag, whether an error has to be raised when retry ends
        :param duration: for how long to wait function to pass in seconds.
        :param interval_timeout: seconds to wait between attempts
        :param error_on_failure: exception to raise when retry fails

        :return: decorated func execution
        """
        self._exceptions = exceptions
        self._duration = duration
        self._interval_timeout = interval_timeout
        self._raise_error_on_failure = raise_error_on_failure
        self._error_on_failure = error_on_failure

    def __call__(self, fn: Callable, *args, **kwargs) -> Any:  # noqa: ARG002
        def wrapped(*args, **kwargs):
            start_time = int(time())
            last_error = None
            while (int(time()) - start_time) < self._duration:
                try:
                    return fn(*args, **kwargs)
                except self._exceptions as e:
                    last_error = e
                    Logger().debug(f"Got an exception while executing {fn}:\nError:\n\t{last_error}")
                sleep(self._interval_timeout)
            if self._raise_error_on_failure:
                raise self._error_on_failure or RuntimeError(
                    f"Timeout {self._duration} to execute {fn.__name__} has passed.\nError:\n\t{last_error}",
                )
            return None

        return wrapped


retry = _Retry
