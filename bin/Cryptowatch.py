import requests
import json
import threading

"""
This class is responsible to retrieve the data from CryptoWatch's API
The API allows only 8 seconds of CPU time in an hour. An average request
takes 0.0025 seconds. This gives us 3200 requests. Round up to 3000 requests
per hour, The refresh rate of data query is 1.2 seconds. 

Set refresh rate to 1.5 as safety boundary

If API allowance is over, a 429 http status code is responded
"""
class Cryptowatch(threading.Thread):
    # Constants
    _URL_PART_1 = "https://api.cryptowat.ch/markets/poloniex/"
    _URL_PART_2 = "/price"
    _MAIN_TAG = "result"
    _SUB_TAG = "price"

    # Instant variables
    _request_url = ""
    _m_select = ""
    _n_select = ""

    def __init__(self, this):
        threading.Thread.__init__(self)
        self._callingClass = this

    def run(self):
        try:
            r = requests.get(self._request_url)
            if r.status_code is 200:
                data = json.loads(r.text)
                data = data[self._MAIN_TAG]
                self._callingClass.newX(float(data[self._SUB_TAG]), self._m_select.upper())
            else:
                self._callingClass.error("CONNECTION ERROR")
        except Exception:
            self._callingClass.error("CONNECTION ERROR")
        return

    def setPair(self, n=None, m=None):
        self._n_select = n
        self._m_select = m
        self._makeURL()

    def _makeURL(self):
        self._request_url = self._URL_PART_1 \
                            + self._m_select.lower() \
                            + self._n_select.lower() \
                            + self._URL_PART_2
        return
