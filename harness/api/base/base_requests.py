from harness.api.base.request_sender import RequestSender
from harness.config.configuration import Config


class BaseRequests:

    def __init__(self, config: Config):
        self._config = config
        self.client = RequestSender(
            pause_duration=config.pause_duration,
            with_new_session=config.with_new_session,
        )

    @property
    def config(self) -> Config:
        return self._config
