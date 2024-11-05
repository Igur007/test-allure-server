from dataclasses import dataclass

from app_confetti import util
from harness.enums.environment import Environment


def str_to_environment(v: str) -> Environment:
    return Environment(v.upper())


def optional_float(v: str) -> float:
    return float(v) if v.lower() != "unset" else None


def optional_bool(v: str) -> bool:
    return v.lower() != "false"


@dataclass
class Config:
    """Configuration class.

    The `env` util function allows for attributes to be retrieved from environment variables.
    """
    env: str = util.env("ENV:dev")

    minio_host: str = util.env("MINIO_HOST:")
    minio_port: int = util.env("MINIO_PORT:", int)
    minio_user: str = util.env("MINIO_USER:")
    minio_secret: str = util.env("MINIO_SECRET:")
    minio_region: str = util.env("MINIO_REGION:")

    pause_duration: float = util.env("PAUSE_DURATION:unset", optional_float)
    with_new_session: bool = util.env("WITH_NEW_SESSION", optional_bool)
    slow_test_max_duration: int = util.env("SLOW_TEST_MAX_DURATION", int)
    enable_post_conditions: bool = util.env("ENABLE_POST_CONDITIONS", optional_bool)
