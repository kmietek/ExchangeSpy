import requests
import json


class CDataMiner:
    @staticmethod
    def __getJson__(method, url):
        req = requests.request(method, url)
        return req.text




