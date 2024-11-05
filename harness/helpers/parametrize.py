from collections.abc import Callable

import pytest


def stored(func: Callable) -> None:
    return pytest.mark.parametrize("product_type", ["stored"])(func)


def streaming(func: Callable) -> None:
    return pytest.mark.parametrize("product_type", ["streaming"])(func)
