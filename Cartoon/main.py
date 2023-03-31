import cv2 as cv2
from sys import argv

def Nothing(val):
    pass

def Save():
    cv2.imwrite("IMG.jpg", IMG)


# CREATE NAMED WINDOW
cv2.namedWindow("Cartoon")

# CREATE TRACKBARS FOR 'BLOCK SIZE' & 'C VALUE'
cv2.createTrackbar("Block Size", "Cartoon", 3, 100, Nothing)
cv2.createTrackbar("C Value", "Cartoon", 3, 100, Nothing)

# READ IMAGE
fileName = argv[1]
OriginalIMG = cv2.imread(fileName)

# CONVERT IMAGE TO GRAY SCALE
GrayIMG = cv2.cvtColor(OriginalIMG, cv2.COLOR_BGR2GRAY)

while True:
    # GET TRACKBARS VALUE
    BlockSize = cv2.getTrackbarPos("Block Size", "Cartoon")
    C = cv2.getTrackbarPos("C Value", "Cartoon")

    # Blure = cv2.blur(GrayIMG, (2, 2))
    Down = cv2.pyrDown(OriginalIMG)
    Up = cv2.pyrUp(Down)

    # BLOCK SIZE % 2 MUST BE != 0
    if BlockSize % 2 == 0: BlockSize -= 1
    Thresh = cv2.adaptiveThreshold(GrayIMG, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, BlockSize, C)

    IMG = cv2.bitwise_and(Up, Up, mask = Thresh)

    cv2.imshow("Cartoon", IMG)

    if cv2.waitKey(1) == ord('q'):
        Save()
        break

cv2.destroyAllWindows()