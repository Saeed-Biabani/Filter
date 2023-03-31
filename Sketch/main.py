import cv2
from sys import argv


def Nothing(x):
    pass

def Save():
    cv2.imwrite(f"RES.jpg", RES)

# CREATE NAMED WINDOW
cv2.namedWindow("Sketch")

# CREATE TRACKBARS FOR 'L' & 'C Scale'
cv2.createTrackbar("L", "Sketch", 0, 255, Nothing)
cv2.createTrackbar("S", "Sketch", 0, 500, Nothing)

# READ IMAGE
fname = argv[1]
img = cv2.imread(fname)

# CONVERT IMAGE TO GRAY SCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# LOGICAL OPERATION NOT
bitNot = cv2.bitwise_not(gray)

# BLURE
blure = cv2.GaussianBlur(bitNot, (17, 17), sigmaX=0, sigmaY=0)

while True:
    # GET TRACKBARS VALUE
    L = cv2.getTrackbarPos("L", "Sketch")
    S = cv2.getTrackbarPos("S", "Sketch")

    RES = cv2.divide(gray, L - blure, scale = S)

    cv2.imshow("Sketch", RES)

    if cv2.waitKey(1) == ord('q'):
        Save()
        break

cv2.destroyAllWindows()