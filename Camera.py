import Bras
import math

class Camera:
    def __init__(self, bras):
        self.bras = bras
        self._x=0
        self._y=0
        self._z=0

    def setPosX(self):
        bras = self.bras
        l1R = bras._L1*math.cos(bras._alpha2)
        l2R = bras._L2*math.cos(bras._alpha3 + bras._alpha2)
        l3R = bras._L3*math.cos(bras._alpha4 + bras._alpha3 + bras._alpha2)
        self._x = math.cos(bras._alpha1)*(l1R + l2R + l3R)

    def setPosY(self):
        bras = self.bras
        l1R = bras._L1 * math.cos(bras._alpha2)
        l2R = bras._L2 * math.cos(bras._alpha3 + bras._alpha2)
        l3R = bras._L3 * math.cos(bras._alpha4 + bras._alpha3 + bras._alpha2)
        self._y = -math.sin(bras._alpha1)*(l1R + l2R + l3R)

    def setPosZ(self):
        bras = self.bras
        self._z = bras._L0 + bras._L1 * math.sin(bras._alpha2) + bras._L2 * math.sin(
            bras._alpha3 + bras._alpha2) + bras._L3 * math.sin(bras._alpha4 + bras._alpha3 + bras._alpha2)

    def actuPos(self):
        self.setPosX()
        self.setPosY()
        self.setPosZ()

    def _getX(self):
        return self._x

    def _getY(self):
        return self._y

    def _getZ(self):
        return self._z

def proc():
    bras = Bras.getABras()
    camera = Camera(bras)
    camera.actuPos()
    print('x =', camera._getX())
    print('y =', camera._getY())
    print('z =', camera._getZ())
if __name__ == '__main__':
    proc()