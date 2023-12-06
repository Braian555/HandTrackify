import cv2
import numpy as np
import HandTrakingModule as htm
import math
import pyautogui

############################################################
wCam, hCam = 640, 480
############################################################

#1
camera = 1

cap = cv2.VideoCapture(camera)

cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7, maxHands=1)

hand_open = False
hand_open2 = False

while True:

    success, img = cap.read()

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        # -------------------------------------------- Minimizar -------------------------------------------------------
        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[0][1], lmList[0][2]

        cv2.circle(img, (x1, y1), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        lengh = math.hypot(x2 - x1, y2 - y1)

        abertPerc = np.interp(lengh, [50, 300], [0, 100])

        # verifica se mão está aberta, se está miniminiza todas as telas
        if round(abertPerc) > 90:
            if not hand_open:
                hand_open = True
                pyautogui.hotkey('win', 'd')
        else:
            hand_open = False
        # -------------------------------------------- Minimizar -------------------------------------------------------

        # -------------------------------------------- Alt + Tab -------------------------------------------------------
        x3, y3 = lmList[20][1], lmList[20][2]
        x4, y4 = lmList[0][1], lmList[0][2]

        cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x4, y4), 15, (255, 0, 255), cv2.FILLED)

        cv2.line(img, (x3, y3), (x4, y4), (255, 0, 255), 3)

        lengh2 = math.hypot(x4 - x3, y4 - y3)

        abertPerc2 = np.interp(lengh2, [50, 300], [0, 100])
        # --------------------------------------------------------------------------------------------------------------

        x5, y5 = lmList[16][1], lmList[16][2]
        x6, y6 = lmList[0][1], lmList[0][2]

        cv2.circle(img, (x5, y5), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x6, y6), 15, (255, 0, 255), cv2.FILLED)

        cv2.line(img, (x5, y5), (x6, y6), (255, 0, 255), 3)

        lengh3 = math.hypot(x6 - x5, y6 - y5)

        trocaPerc = np.interp(lengh3, [50, 300], [0, 100])

        # --------------------------------------------------------------------------------------------------------------
        print("Primeiro: ", round(abertPerc))
        print("Segundo: ", round(abertPerc2))
        print("Terceiro: ", round(trocaPerc))

        # verifica se a mão está aberta para alternar entre as janelas
        if round(abertPerc2) > 50:
            if not hand_open2:
                hand_open2 = True
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                if round(trocaPerc) >= 25:
                    pyautogui.keyUp('alt')

                if round(trocaPerc) < 10:
                    pyautogui.keyUp('enter')

        else:
            hand_open2 = False
        # -------------------------------------------- Alt + Tab -------------------------------------------------------

    cv2.rectangle(img, (50, 150), (85, 360), (255,0,0), 3)

    cv2.imshow("img", img)

    k = cv2.waitKey(1) & 0xFF

    if k == 27 or k == 13:
        break
