import math
from Servo import Servo
from adafruit_servokit import ServoKit
import numpy as np
import time

class Bras:
    
    def __init__(self, camera):
        self.camera = camera
        print("config d")
        
        self.posInit = [90, 90, 45, 45, 0]
        # ~ self.posRepos = [0, 130, 0, 0, 0]
        self.posRepos = [90, 90, 90, 80, 90]
        
        self.nbServos = 5
        self._L0 = 7.9
        self._L1 = 12.5
        self._L2 = 12.5
        self._L3 = 18.5
        self._alpha0 = 90
        self._alpha1 = 90
        self._alpha2 = 90
        self._alpha3 = 80
        self._alpha4 = 0
        self.pca = ServoKit(channels= 16)
        self.servos = []
        for i in range(self.nbServos):
            self.servos.append(Servo(i, self.pca, self))
        for i in range(self.nbServos-1, -1, -1):
            ok = self.servos[i].goToAngle(self.posInit[i])
            if ok:
                if i == 0:
                    self._alpha0 = self.posInit[i]
                elif i == 1:
                    self._alpha1 = self.posInit[i]
                elif i == 2:
                    self._alpha2 = self.posInit[i]
                elif i == 3:
                    self._alpha3 = self.posInit[i]
                elif i == 4:
                    self._alpha4 = self.posInit[i]
            time.sleep(0.2)
            
        print("config f")

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
        
    def goRepos(self):
        for i in range(self.nbServos):
            self.servos[i].goToAngle(self.posRepos[i])
            time.sleep(0.5)
            self.servos[i].angle=None
            #print("Servo", i)
            
    def goInit(self):
        for i in range(self.nbServos-1, -1, -1):
            ok = self.servos[i].goToAngle(self.posInit[i])
            if ok:
                if i == 0:
                    self._alpha0 = self.posInit[i]
                elif i == 1:
                    self._alpha1 = self.posInit[i]
                elif i == 2:
                    self._alpha2 = self.posInit[i]
                elif i == 3:
                    self._alpha3 = self.posInit[i]
                elif i == 4:
                    self._alpha4 = self.posInit[i]
            time.sleep(0.2)
            
    def alterAlpha0(self,vue):
        pas = 1
        if (vue=='D'):
            ok = self.servos[0].goToAngle(self._alpha0 - pas)
            #if ok:
             #   self._alpha0=self._alpha0-pas
        if (vue=='G'):
            ok = self.servos[0].goToAngle(self._alpha0+pas)
            #if ok:
             #   self._alpha0=self._alpha0+pas
        self._alpha0 = self.servos[0].angle
        #return self._alpha0        truc a enlever


    def alterAlpha2(self, vue):
        if (vue=='B'):
            ok = self.servos[2].goToAngle(self._alpha2 - 1)
            #if ok:
             #   self._alpha2=self._alpha2-1
        if (vue=='H'):
            ok = self.servos[2].goToAngle(self._alpha2 + 1)
            #if ok:
             #   self._alpha2=self._alpha2+1
        self._alpha2 = self.servos[2].angle
        #return self._alpha1


    def alterAlpha3(self, alpha1,alpha2):
        ok = self.servos[3].goToAngle(180-alpha2-alpha1)
        #if ok:
         #   if abs(self._alpha3 - self.servos[3].angle) < 3:
          #      self._alpha3=180-alpha2 - alpha1
           #     #print("alpha3 =",self._alpha3)
            #else:
        self._alpha3=self.servos[3].angle
        #return self._alpha3

if __name__ == '__main__':
    bras = Bras()
    time.sleep(3)
    bras.goRepos()
