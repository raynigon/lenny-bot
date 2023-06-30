import requests

from ..config.config import LennyBotActionConfig
from .iaction import IAction


class DownloadResourcesAction(IAction):

    def __init__(self, name, source_version, target_version, config: LennyBotActionConfig) -> None:
        self._name = name
        self._source_version = source_version
        self._target_version = target_version
        self._url = config.url
        self._target_path = config.target

    @property
    def application(self) -> str:
        return self._name

    @property
    def source_version(self) -> str:
        return self._source_version

    @property
    def target_version(self) -> str:
        return self._target_version

    def run(self):
        download_url = self._url.replace("{{version}}", self._target_version)
        response = requests.get(download_url)
        if response.status_code != 200:
            raise Exception("Unable to download resources")
        with open(self._target_path, "w") as file_ptr:
            file_ptr.write(response.text)