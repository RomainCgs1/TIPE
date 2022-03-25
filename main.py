import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    closerX = 0
    closerY = 0
    closerW = 0
    closerH = 0
    closerCenter = (0, 0)

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
    if middleX < closerCenter[0] < middleX + areaSide and middleY < closerCenter[1] < middleY + areaSide:
        print("Centre !")
        cv2.circle(img, closerCenter, 10, (255, 255, 255))
    else:
        if closerCenter[0] <= rendWidth / 2:
            print("Droite")
            cv2.circle(img, closerCenter, 10, (0, 0, 255))
        else:
            print("Gauche")
            cv2.circle(img, closerCenter, 10, (0, 255, 0))

        if closerCenter[1] >= rendHeight / 2:
            print("     Bas")
        else:
            print("     Haut")

    # Display
    cv2.imshow('Flux video', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release the VideoCapture object
cap.release()
