# =============================================================================
# Copyright 2023-2025 Autor da HandTrackify.
#
# Arquivo: hand_command.py
# Criado por: Braian E.C. Vidal
# Data de Criação: 08/12/2023
# Última Modificação por: Braian E.C. Vidal
# Data da Última Modificação: 10/12/2023
# Licença: GNU General Public License v3.0
# Link da Licença: https://github.com/Braian555/HandTrackify/blob/main/LICENSE
#
# =============================================================================

# Bibliotecas padrão
import math
import subprocess
import time

# Bibliotecas de terceiros
import cv2
import pyautogui
import keyboard

# Modulos personalizados
import hand_tracking_module as htm
import calculator

# Funções de melhor leitura
def abrir_calculadora():
    try:
        calculator.Calculadora().mainloop()
    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado na pasta {diretorio_atual}.')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Configuração da câmera
wCam, hCam = 1280, 720

# Configuração da fonte para exibição de texto
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

# Número da câmera (0 para câmera padrão)
camera = 0

# Inicialização da câmera
cap = cv2.VideoCapture(camera)
cap.set(3, wCam)
cap.set(4, hCam)

# Inicialização do detector de mãos
detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# Variaveis de controle para o loop
gestOn = False
thumb_executed = False
index_executed = False
middle_executed = False
ring_executed = False
pinky_executed = False

while True:

    # Captura de um frame da câmera
    success, img = cap.read()

    # Encontrar e desenhar mãos na imagem
    img = detector.findHands(img)

    # Obter a posição das landmarks das mãos
    lmList = detector.findPosition(img, draw=False)

    # Verificar se landmarks foram encontradas
    if len(lmList) != 0:

        # Obtenção das coordenadas das articulações da mão
        THM = x10, y10 = lmList[2][1], lmList[2][2]  # THUMB_MCP
        INP = x20, y10 = lmList[6][1], lmList[6][2]  # INDEX_FINGER_PIP
        MIP = x30, y10 = lmList[10][1], lmList[10][2]  # MIDDLE_FINGER_PIP
        RIP = x40, y10 = lmList[14][1], lmList[14][2]  # RING_FINGER_PIP
        PIP = x50, y10 = lmList[18][1], lmList[18][2]  # PINKY_PIP

        # Coordenadas das pontas dos dedos
        THT = x11, y11 = lmList[4][1], lmList[4][2]  # THUMB_TIP
        INT = x21, y21 = lmList[8][1], lmList[8][2]  # INDEX_FINGER_TIP
        MIT = x31, y31 = lmList[12][1], lmList[12][2]  # MIDDLE_FINGER_TIP
        RIT = x41, y41 = lmList[16][1], lmList[16][2]  # RING_FINGER_TIP
        PIT = x51, y51 = lmList[20][1], lmList[20][2]  # PINKY_TIP

        # Desenhar círculos nas pontas dos dedos
        cv2.circle(img, THT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, INT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, MIT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, RIT, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, PIT, 5, (255, 0, 255), cv2.FILLED)

        # Variável para contar dedos levantados
        dedos_levantados = 0

        # Comparação para verificar se o dedo está acima do indicador
        if THT[1] > THM[1]:
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

        # Verifica se o usuário quer usar navegação por gestos
        if gestOn == False:
            cv2.putText(img, 'Ativar gestos clique "G"', (50, 113), font, fontScale, color, thickness, cv2.LINE_AA)

        # Usando a biblioteca keyboard para detectar a tecla 'G'
        if keyboard.is_pressed('g') and not gestOn:
            gestOn = True
        
        if gestOn:
            # Executa os gestos de acordo com a quantidade de dedos
            thumb_up = THT[1] > THM[1]
            index_up = INT[1] < INP[1]
            middle_up = MIT[1] < MIP[1]
            ring_up = RIT[1] < RIP[1]
            pinky_up = PIT[1] < PIP[1]

            # Configuração para o dedo polegar (THUMB)
            if thumb_up and not thumb_executed:
                abrir_calculadora()
                thumb_executed = True
            elif not thumb_up and thumb_executed:
                thumb_executed = False

            # Configuração para o dedo indicador (INDEX)
            if index_up and not index_executed:
                subprocess.run(["notepad.exe"])
                index_executed = True
            elif not index_up and index_executed:
                index_executed = False

            # Configuração para o dedo médio (MIDDLE)
            if middle_up and not middle_executed:
                pyautogui.hotkey('win', 'e')
                middle_executed = True
            elif not middle_up and middle_executed:
                middle_executed = False

            # Configuração para o dedo anelar (RING)
            if ring_up and not ring_executed:
                pyautogui.hotkey('win', 'p')
                ring_executed = True
            elif not ring_up and ring_executed:
                ring_executed = False

            # Configuração para o dedo mínimo (PINKY)
            if pinky_up and not pinky_executed:
                pyautogui.hotkey('prtscr')
                pinky_executed = True
            elif not pinky_up and pinky_executed:
                pinky_executed = False
            
    # Exibir a imagem com as marcações
    cv2.imshow("img", img)

    # Encerrar o programa se a tecla ENTER for pressionada
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == 13:
        print("Você encerrou o programa")
        break
