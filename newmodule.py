import cv2
import mediapipe as mp
import time
import handtrackingmodule as htm

cTime = 0
pTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    sucess, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (244, 0, 321), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)