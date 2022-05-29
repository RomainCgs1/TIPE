import time
from adafruit_servokit import ServoKit


class Servo:
	
	def __init__(self, indx, pca, bras):
		self.bras = bras
		self.nbServos = 5

		self._MIN_IMP = [500, 500, 500, 500, 500]
		self._MAX_IMP = [2500, 2500, 2500, 2500, 2500]
		self._MIN_ANG = [0, 20, 10, 0, 0]
		self._MOW_ANG = [90, 90, 90, 80, 90]
		self._MAX_ANG  =[179, 150, 170, 178, 180]
		
		self.pca = pca
		self.pca.servo[indx].set_pulse_width_range(self._MIN_IMP[indx] , self._MAX_IMP[indx])
		self.srv = self.pca.servo[indx]
		self.angle = self._MOW_ANG[indx]
		self.indx = indx
	
	def goToAngle(self, angle): #problèmes dûs à une mauvaise connaisance de la position au départ et de la position de début de mouvement
		print("angle servo", self.indx,":", self.angle, "°")
		s = False
		#print('angle demandé pour le moteur', self.indx, ':', angle)
		self.bras.camera.actuPos(self.bras)
		#print(self.bras.camera._getZ())
		#print(angle > self._MAX_ANG[self.indx])
		#print(angle < self._MIN_ANG[self.indx])
		#print(self.bras.camera._getZ() < 5)
		if not (angle > self._MAX_ANG[self.indx] or angle < self._MIN_ANG[self.indx] or self.bras.camera._getZ() < 5):
			print("on bouge")
			if self.angle > angle+1:
				incr = -1
			else:
				incr = 1
			for i in range(self.angle, angle+1, incr):
				#print(i)
				self.srv.angle = i
				time.sleep(0.02) #0.05 est bien
			self.angle = angle
			s = True
		#print(s)
		return s
