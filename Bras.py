import math


class Bras:

    def __init__(self):
        self._L0 = 1
        self._L1 = 2
        self._L2 = 2
        self._L3 = 1
        self._alpha1 = 0
        self._alpha2 = math.pi
        self._alpha3 = 0
        self._alpha4 = 0

    def _getL0(self):
        return self._L0

    def _getL1(self):
        return self._L1

    def _getL2(self):
        return self._L2

    def _getL3(self):
        return self._L3

    def _getAlpha1(self):
        return self._alpha1

    def _getAlpha2(self):
        return self._alpha2

    def _getAlpha3(self):
        return self._alpha3

    def _getAlpha4(self):
        return self._alpha4

def getABras():
    return Bras()