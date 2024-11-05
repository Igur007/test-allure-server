from enum import Enum


class Environment(Enum):
    LOCAL: str = "LOCAL"
    DEV: str = "DEV"
    TEST: str = "TEST"
    STAGE: str = "STAGE"
