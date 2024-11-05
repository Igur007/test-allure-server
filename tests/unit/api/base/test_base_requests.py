from unittest import mock

import allure
from harness.api.base import base_requests


@allure.parent_suite("[Unit] Tests")
@allure.feature("Config")
class TestBaseRequests:

    def test_config(self, config):
        mock_config = mock.Mock()
        br = base_requests.BaseRequests(config)
        br._config = mock_config

        assert br.config != config
        assert br.config == mock_config
