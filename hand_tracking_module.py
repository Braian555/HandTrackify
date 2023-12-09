import cv2
import mediapipe as mp
import time
import math

class handDetector():
    def __init__(self, mode=False, modelComplexity=1, maxHands=2, detectionCon=0.5, trackCon=0.5):
        # Inicializa o detector de mãos com parâmetros configuráveis
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # Configura o módulo hands da Mediapipe
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        # Converte a imagem para o formato RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Processa a imagem em busca de mãos
        self.results = self.hands.process(imgRGB)

        # Verifica se mãos foram detectadas
        if self.results.multi_hand_landmarks:
            # Desenha as landmarks e as conexões na imagem se a flag 'draw' estiver configurada
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        # Lista para armazenar as posições das landmarks
        lmlist = []

        # Verifica se mãos foram detectadas
        if self.results.multi_hand_landmarks:
            # Obtém informações sobre a mão específica indicada por 'handNo'
            myHand = self.results.multi_hand_landmarks[handNo]
            # Itera sobre as landmarks da mão
            for id, lm in enumerate(myHand.landmark):
                # Obtém as coordenadas normalizadas e as converte para as coordenadas da imagem
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # Adiciona as informações à lista
                lmlist.append([id, cx, cy])

                # Desenha um círculo na posição da landmark se a flag 'draw' estiver configurada
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmlist

    def findDistance(self, p1, p2, img, draw=True):
        # Obtém as coordenadas das landmarks referentes aos pontos p1 e p2
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        # Calcula o ponto médio e o desenha se a flag 'draw' estiver configurada
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        # Calcula a distância euclidiana entre os pontos p1 e p2
        length = math.hypot(x2 - x1, y2 - y1)
        return length, img, [x1, y1, x2, y2, cx, cy]
