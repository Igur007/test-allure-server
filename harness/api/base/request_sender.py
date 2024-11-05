import time
from json import dumps
from pprint import pformat

import requests
from requests import Response

from harness.config.logger import Logger


class RequestSender:
    logger = Logger()
    session = requests.Session()

    def __init__(self, pause_duration: float = None, with_new_session: bool = False):
        self.pause_duration = pause_duration
        if with_new_session:
            self.create_new_session()

    def create_new_session(self) -> None:
        RequestSender.session = requests.Session()

    def set_authorization(self, authorization: str) -> None:
        self.session.headers.update({"authorization": authorization})

    def send(self, method: str, url: str, params: dict = None, data: dict = None, json: dict = None,
             headers: dict = None, cookies: dict = None, files: dict = None,
             auth: dict = None, timeout: float = None, allow_redirects: bool = True, proxies: dict = None,
             hooks: dict = None, stream: dict = None, verify: bool = None, cert: bool = None,
             log_response: bool = True) -> Response:

        if self.pause_duration and self.pause_duration > 0:
            time.sleep(self.pause_duration)
        self.logger.debug(f"\nSession: {id(self.session)}")
        self.logger.info(f"Sending HTTP {method} to: {url}")
        self.logger.info(f"Headers: {pformat(headers or {})}")
        self.logger.info(f"Session headers: {pformat(self.session.headers or {})}")
        if json is not None:
            self.logger.info(f"Body:\n {dumps(json, indent=4, sort_keys=True)}")
        if data is not None:
            self.logger.info(f"Data:\n {dumps(data, indent=4, sort_keys=True)}")
        if params is not None:
            self.logger.info(f"Params:\n {dumps(params, indent=4, sort_keys=True)}")
        if files is not None:
            self.logger.info(f"Files:\n {pformat(files)}")

        self.session.verify = verify or False
        response = self.session.request(
            method=method, url=url, params=params, data=data, json=json, headers=headers,
            cookies=cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies,
            hooks=hooks, stream=stream, verify=verify, cert=cert)
        self.logger.info(f"Response status code: {response.status_code}")
        if log_response:
            if response.text and "json" in response.headers.get("Content-Type"):
                self.logger.info(f"Response text:\n {dumps(response.json(), indent=4, sort_keys=True)}")
            else:
                self.logger.info(f"Response text:\n {response.text}")
        return response
