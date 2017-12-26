import requests
import threading

import bin.Helpers as helper

"""
This class is responsible to retrieve the Best Bid (INR) data from Coindelta 
"""
class Coindelta(threading.Thread):
    # Constants
    _API_URL = "https://coindelta.com/api/v1/public/getticker/"
    _SUFFIX = "-inr"
    _LOOK_TAG = "MarketName"
    _GET_TAG = "Bid"

    def __init__(self, _this):
        threading.Thread.__init__(self)
        self._calling_class = _this
        self._get_id = ""
        return

    def run(self):
        if self._get_id != "":
            try:
                r = requests.get(self._API_URL)
                value = self._parse(r.text)
                self._calling_class.newY(value, self._get_id.upper())
            except Exception:
                self._calling_class.error("CONNECTION ERROR")
        else:
            self._calling_class.error("CURRENCY NOT SELECTED")
        return

    def set_id(self, _id):
        self._get_id = _id
        return

    def _parse(self, text):
        data = helper.loadJson(text=text)
        look_for = self._get_id.lower() + "" + self._SUFFIX
        for item in data:
            if item[self._LOOK_TAG] == look_for:
                return item[self._GET_TAG]
        return None
