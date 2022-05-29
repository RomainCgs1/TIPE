from Bras import Bras
import math
import cv2

def dToR(angle):
    return angle * math.pi / 180

class Camera:
    def __init__(self):
        self._x=0
        self._y=0
        self._z=50

    def setPosX(self, bras):
        a0 = dToR(bras._alpha0)
        a1 = dToR(bras._alpha1)
        a2 = dToR(bras._alpha2)
        a3 = dToR(bras._alpha3)
        
        l1R = bras._L1*math.cos(a1)
        l2R = bras._L2*math.cos(a2)
        l3R = bras._L3*math.cos(a3)
        self._x = math.cos(a0)*(l1R + l2R + l3R)

    def setPosY(self, bras):
        a0 = dToR(bras._alpha0)
        a1 = dToR(bras._alpha1)
        a2 = dToR(bras._alpha2)
        a3 = dToR(bras._alpha3)
        
        l1R = bras._L1 * math.cos(a1)
        l2R = bras._L2 * math.cos(a2)
        l3R = bras._L3 * math.cos(a3)
        self._y = -math.sin(a0)*(l1R + l2R + l3R)

    def setPosZ(self, bras):
        a0 = dToR(bras._alpha0)
        a1 = dToR(bras._alpha1)
        a2 = dToR(bras._alpha2)
        a3 = dToR(bras._alpha3)
        
        self._z = bras._L0 + bras._L1 * math.sin(a1) + bras._L2 * math.sin(
            a2) + bras._L3 * math.sin(a3)

    def actuPos(self, bras):
        
        self.setPosX(bras)
        print("angle 0 :", bras._alpha0)
        print("angle 1 :", bras._alpha1)
        print("angle 2 :", bras._alpha2)
        print("angle 3 :", bras._alpha3)
        self.setPosY(bras)
        self.setPosZ(bras)

    def _getX(self):
        return self._x

    def _getY(self):
        return self._y

    def _getZ(self):
        return self._z

def proc(bras):
    camera = Camera(bras)
    camera.actuPos()
    print('x =', camera._getX())
    print('y =', camera._getY())
    print('z =', camera._getZ())
    
    
def vue(bras):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)
    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Capture frame-by-frame
        ret, img = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        closerX = 0
        closerY = 0
        closerW = 0
        closerH = 0
        closerCenter = (-1, -1)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            x0 = int(x + w / 2)
            y0 = int(y + h / 2)
            centerCoord = (x0, y0)

            # get closer face
            if w > closerH:
                closerX = x
                closerY = y
                closerW = w
                closerH = h
                closerCenter = centerCoord

        rendWidth = img.shape[1]
        rendHeight = img.shape[0]

        # middle area
        areaSide = 100
        middleX = int((rendWidth - areaSide) / 2)
        middleY = int((rendHeight - areaSide) / 2)

        # display middle area
        cv2.rectangle(img, (middleX, middleY), (middleX + areaSide, middleY + areaSide), (200, 200, 0), 2)

        # print a circle in the middle of the closer face

        # check if closer face is in the middle area
        V = ['', '']
        if middleX < closerCenter[0] < middleX + areaSide and closerCenter[0] >= 0:
            print("Centre !")
            V[0]='i'
            #cv2.circle(img, closerCenter, 10, (255, 255, 255))
        elif closerCenter[0] <= rendWidth / 2 and closerCenter[0] >= 0:
            print("Droite")
            V[0]='D'
            #cv2.circle(img, closerCenter, 10, (0, 0, 255))
        elif closerCenter[0] >= 0:
            print("Gauche")
            V[0]='G'
            #cv2.circle(img, closerCenter, 10, (0, 255, 0))
        if middleY < closerCenter[1] < middleY + areaSide and closerCenter[0] >= 0:
            print("Centre !")
            V[1]='i'
            #cv2.circle(img, closerCenter, 10, (255, 255, 255))
        elif closerCenter[1] >= rendHeight / 2 and closerCenter[1] >= 0:
            print("     Bas")
            V[1]='B'
        elif closerCenter[0] >= 0:
            print("     Haut")
            V[1]='H'

        #changer les angles
        bras.alterAlpha0(V[0])
        bras.alterAlpha2(V[1])
        bras.alterAlpha3(bras._alpha1, bras._alpha2)

        # Display
        cv2.imshow('Flux video', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        if k == 99:
            print("Reinit")
            bras.goInit()
        
    # Release the VideoCapture object
    cap.release()
    
    
if __name__ == '__main__':
    camera = Camera()
    bras = Bras(camera)
    vue(bras)
    bras.goRepos()
