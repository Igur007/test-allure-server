from getpass import getuser
import json
import logging.config
from pathlib import Path

from harness.helpers.singleton import Singleton


PATH_TO_REPOSITORY: Path = Path(__file__).parent.parent.parent
PATH_TO_HARNESS: Path = Path(PATH_TO_REPOSITORY, "harness")
DEFAULT_PATH_TO_LOGS_FOLDER: Path = Path(PATH_TO_HARNESS, "logs")
DEFAULT_PATH_TO_CONFIG_FOLDER: Path = Path(PATH_TO_HARNESS, "config")
DEFAULT_PATH_TO_LOGGING_JSON: Path = Path(DEFAULT_PATH_TO_CONFIG_FOLDER, "logging.json")


class Logger:
    """Displays and writes to log file in different formats"""
    __metaclass__ = Singleton

    def __new__(
        cls,
        path_to_logging_json: Path = DEFAULT_PATH_TO_LOGGING_JSON,
        path_to_logs_folder: Path = DEFAULT_PATH_TO_LOGS_FOLDER,
        default_level: int = logging.DEBUG):
        return cls.setup_logging(path_to_logging_json, path_to_logs_folder, default_level)

    @classmethod
    def setup_logging(cls, path_to_logging_json: Path, path_to_logs_folder: Path, default_level: int):
        """Setup logging configuration

        :param path_to_logging_json: default path to logging.json configuration file
        :param path_to_logs_folder: default path to folder with log files
        :param default_level: default level of logging
        :return: logging object
        """
        cls.create_log_folder(path_to_logs_folder)

        if path_to_logging_json.exists():
            with path_to_logging_json.open(mode="rt") as f:
                config = json.load(f)
                cls.add_path_to_logs_folder_to_log_filenames_from_json_config(config, path_to_logs_folder)
            logging.config.dictConfig(config)
            logging.debug(f"JSON CONFIG defined: {path_to_logging_json} path to logs folder: {path_to_logs_folder}")
        else:
            logging.basicConfig(level=default_level)
            logging.debug("BASIC CONFIG")
        return logging.getLogger(getuser())

    @classmethod
    def create_log_folder(cls, path_to_logs_folder: Path):
        """creates folder to write logs, if it does not exist

        :return: nothing to return
        """
        if not path_to_logs_folder.exists():
            path_to_logs_folder.mkdir(parents=True)

    @classmethod
    def add_path_to_logs_folder_to_log_filenames_from_json_config(cls, config: dict, path_to_logs_folder: Path):
        """adds DEFAULT_PATH_TO_LOGS_FOLDER to all handlers, which have "filename" key

        :param config: data as dict from logging.json configuration file
        :param path_to_logs_folder: default path to folder with log files
        :return: modified config dictionary
        """
        for handler in config["handlers"]:
            filename = config["handlers"][handler].get("filename")
            if filename:
                full_path_to_log_file = Path(path_to_logs_folder, config["handlers"][handler].get("filename"))
                config["handlers"][handler]["filename"] = full_path_to_log_file
