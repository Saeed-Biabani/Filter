import cv2 as cv2
from sys import argv
from numpy import zeros, uint32

# USE CASCADE CLASSIFIER FOR FACE DETECTION
Face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# READ IMAGE
img = cv2.imread(argv[1])

# CONVERT IMAGE TO GRAY SCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# DETECT FACE USING CASCADE CLASSIFIER
Faces = Face.detectMultiScale(gray, 1.1, 4)

# BLURE FACE REGION
for (x, y, w, h) in Faces:
        img[y:y+h, x:x+w] = cv2.blur(img[y:y+h, x:x+w], (25, 25))

cv2.imwrite("Censored.jpg", img)