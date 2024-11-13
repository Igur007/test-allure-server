from time import sleep

import allure
import pytest
from harness.api.base import base_requests


@allure.parent_suite("[E2E] Tests")
@allure.feature("e2e")
class TestE2ERequests:

    @pytest.mark.parametrize('execution_number', range(1, 867))
    def test(self, config, execution_number):
        br = base_requests.BaseRequests(config)
        for _ in range(25):
            br.client.send(
                "GET",
                'https://cluster02.neosdata.cloud/api/gateway/v2/output/d669e53f-6fe3-4727-b0f9-e3be700da88f/journal',
            )
            sleep(0.2)
