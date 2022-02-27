import requests

from source.settings import FORTNITE_IO_API_SETTINGS


class FortniteIoApiClient(object):
    def __init__(self, api_settings):
        self.base_url = api_settings["base_url"]
        self.api_key = api_settings["api_key"]
        self.timeout = api_settings["timeout"]

    def _get(self, url_suffix):
        headers = {"Authorization": self.api_key}
        response = requests.get(url=self.base_url + url_suffix, headers=headers)
        return response

    def get_stats(self, io_account_id):
        return self._get(f"/v1/stats?account={io_account_id}")

    def get_lookup(self, name):
        return self._get(f"/v1/lookup?username={name}")

    def get_shop(self):
        return self._get(f"/v2/shop?lang=en")


FORTNITE_IO_API_CLIENT = FortniteIoApiClient(api_settings=FORTNITE_IO_API_SETTINGS)
