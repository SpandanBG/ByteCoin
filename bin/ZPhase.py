"""
This class is responsible to handle the final phase of the application
Finding the ratio = Y:X
Getting user input => Z
And Calculation of the BTC Process Rate = Z*(Y/X)
"""
class ZPhase:
    def __init__(self):
        self._x = 0.0
        self._y = 0.0
        self._z = 0.0
        self._ratio = 0.0

    def setXandY(self, x, y):
        self._x = x
        self._y = y
        try:
            self._ratio = float(y)/float(x)
        except Exception:
            pass

    def ratio(self):
        return self._ratio

    def setBuyRate(self, z):
        try:
            self._z = float(z)
            return True
        except Exception:
            self._Z = 0.0
            return False

    def processRate(self):
        return float(self._z)*float(self._ratio)