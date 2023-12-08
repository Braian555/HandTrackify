import cv2
import numpy as np
import hand_traking_module as htm
import math
import pyautogui
import time

############################################################
wCam, hCam = 640, 480
############################################################

############################################################
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2
############################################################

camera = 0

cap = cv2.VideoCapture(camera)

cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7, maxHands=1)

test = True

while test == True:

    success, img = cap.read()

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        
        # THUMB_MCP
        THM  = x10, y10 = lmList[2][1], lmList[2][2]
        
        # INDEX_FINGER_PIP
        INP = x20, y10 = lmList[6][1], lmList[6][2]
        
        # MIDDLE_FINGER_PIP
        MIP = x30, y10 = lmList[10][1], lmList[10][2]
        
        # RING_FINGER_PIP
        RIP = x40, y10 = lmList[14][1], lmList[14][2]
        
        # PINKY_PIP
        PIP = x50, y10 = lmList[18][1], lmList[18][2]
        
        #---------------------- TOP FINGER BELOW ----------------------
        
        # THUMB_TIP
        THT = x11, y11 = lmList[4][1], lmList[4][2]
        
        # INDEX_FINGER_TIP
        INT = x21, y21 = lmList[8][1], lmList[8][2]
        
        # MIDDLE_FINGER_TIP
        MIT = x31, y31 = lmList[12][1], lmList[12][2]
        
        # RING_FINGER_TIP
        RIT = x41, y41 = lmList[16][1], lmList[16][2]
        
        # PINKY_TIP
        PIT = x51, y51 = lmList[20][1], lmList[20][2]
        
        # Circle in tip of finger
        cv2.circle(img, THT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, INT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, MIT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, RIT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, PIT, 5, (255, 0, 255), cv2.FILLED)

        # Variável para contar dedos levantados
        dedos_levantados = 0

        # Comparação correta para verificar se o dedo está acima do indicador
        if THT > THM:
            dedos_levantados += 1

        if INT[1] < INP[1]:
            dedos_levantados += 1

        if MIT[1] < MIP[1]:
            dedos_levantados += 1

        if RIT[1] < RIP[1]:
            dedos_levantados += 1

        if PIT[1] < PIP[1]:
            dedos_levantados += 1

        # Exibir o número total de dedos levantados
        cv2.putText(img, f'Dedos Levantados: {dedos_levantados}', (50, 50), font, fontScale, color, thickness, cv2.LINE_AA)


   
    cv2.imshow("img", img)

    # Break if use ESC or ENTER
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == 13:
        print("You stop the program")
        test = False
