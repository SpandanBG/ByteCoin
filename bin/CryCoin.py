import bin.Helpers as helper

"""
This class is responsible to allow a selection between the options
of Crypto Currencies. The available list is in the config/cryptocurrencies.json
file.

Apart from these it also returns the Currency with which the above mentioned
will be compared with
"""
class CryCoin:
    # Constants
    _JSON_FILE = "config/cryptocurrencies.json"
    _N_TAG = "primaryCryCoin"
    _M_TAG = "secondCryCoin"

    # Instant variables
    n_select = ""
    m_select = ""

    # Initializer
    def __init__(self):
        self._cryCoinData = helper.loadJson(path=self._JSON_FILE)
        self.n_set = self._cryCoinData[self._N_TAG]
        self.m_set = self._cryCoinData[self._M_TAG]

    # Get N Set
    def getNSet(self):
        return self.n_set

    # Get M Set
    def getMSet(self):
        return self.m_set

    # Make N Select
    def setNselect(self, key=None, value=None):
        if value is not None and value in self.n_set.values():
            self.n_select = value
        elif key is not None and key in self.n_set.keys():
            self.n_select = self.n_set[key]
        else:
            return False
        return True

    # Make M Select
    def setMselect(self, key=None, value=None):
        if value is not None and value in self.m_set.values():
            self.m_select = value
        elif key is not None and key in self.m_set.keys():
            self.m_select = self.m_set[key]
        else:
            return False
        return True
