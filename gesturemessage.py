import cv2
import numpy as np
import time
import handtrackingmodule as htm
import math
import pywhatkit as pt
import datetime

wCam, hCam = 580, 320

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector= htm.handDetector(detectionCon=0.15)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4],lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2) // 2, (y1+y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        lenght=math.hypot(x1-x2, y1-y2)
        print(lenght)

        if lenght<23:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

            now = datetime.datetime.now()
            pt.sendwhatmsg('+91 {mobileno}','sos',now.hour,now.minute+1)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (244, 0, 321), 3)


    cv2.imshow("img", img)
    if cv2.waitKey(1)==ord('q'):
        break
