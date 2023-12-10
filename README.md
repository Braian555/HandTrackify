# Hand Gesture Control Project

Este é um projeto que utiliza a biblioteca Mediapipe para calcular a contagem de dedos através da detecção de mãos. O script principal, `hand_tracking_module`, é um módulo de detecção de mãos que integra algoritmos avançados para interpretar gestos. Sua abordagem modular facilita a aplicação em diversas áreas, como jogos e automação, representando uma fusão precisa e inovadora entre detecção de mãos e interação gestual.

Para demonstrar o poder deste projeto, foi criado um script que calcula a quantidade de dedos levantados e executa comandos diferentes no computador, desde abrir o notebook até abrir o navegador principal.

## Requisitos

- Desktop: Windows, Mac, Linux. IoT: Raspberry OS 64-bit.
- Python: versão 3.8 - 3.11.
- PIP: versão 20.3+
- OpenCV
- Mediapipe
- PyAutoGUI

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/Braian555/HandTrackify.git
    cd HandTrackify
    ```

2. Instale as dependências:

    ```bash
    pip install opencv-python
    pip install mediapipe
    pip install pyautogui
    pip install keyboard
    ```

3. Permita que o aplicativo acesse a câmera.

## Uso

Execute o script Python para iniciar o controle de gestos:

    ```bash
    python hand_command.py
    ```

Uma janela com a câmera será exibida, onde você pode ativar as funções de controle de tela com a tecla F.

## Configuração

O projeto começa com variáveis globais que são usadas para medir a proporção da janela da câmera, as formatações do texto, entre outras.

Deixo abaixo algumas explicações de trechos criticos do código:

# Módulo de Detecção de Mãos (`hand_traking_module.py`)

O arquivo `hand_traking_module.py`, que é um arquivo com os módulos que são utilizados no projeto para detectar mãos e extrair informações relevantes. Todos os módulos utilizam a biblioteca Mediapipe para realizar a detecção de mãos.

**Explicação:**
- O módulo `handDetector` é uma classe que encapsula a funcionalidade de detecção de mãos utilizando a Mediapipe.
- O método `findHands` processa a imagem e, se mãos forem detectadas, desenha as landmarks e conexões na imagem.
- O método `findPosition` retorna uma lista com as coordenadas das landmarks da mão, permitindo a identificação de pontos-chave.
- O método `findDistance` calcula a distância euclidiana entre dois pontos específicos das landmarks.

Esses módulos são cruciais para a detecção de mãos e a extração de informações relevantes para o controle de gestos no projeto.

# Variáveis dos Dedos

No trecho de código abaixo, são definidas variáveis para as diferentes partes dos dedos detectadas pela biblioteca Mediapipe. Essas variáveis representam as coordenadas (x, y) de pontos específicos em cada dedo.

```python
# THUMB_MCP
THM = x10, y10 = lmList[2][1], lmList[2][2]

# INDEX_FINGER_PIP
INP = x20, y10 = lmList[6][1], lmList[6][2]

# MIDDLE_FINGER_PIP
MIP = x30, y10 = lmList[10][1], lmList[10][2]

# RING_FINGER_PIP
RIP = x40, y10 = lmList[14][1], lmList[14][2]

# PINKY_PIP
PIP = x50, y10 = lmList[18][1], lmList[18][2]

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
```

Essas variáveis representam os pontos-chave das articulações e pontas dos dedos detectados. Cada variável é uma tupla contendo as coordenadas (x, y) correspondentes ao ponto no espaço da imagem.

**Importância:**
- **Ponto MCP (Metacarpo):** Representa a base do dedo.
- **Ponto PIP (Interfalangeana Proximal):** Representa a articulação intermediária do dedo.
- **Ponto TIP (Ponta):** Representa a ponta do dedo.

Para verificar a posição dos dedos, analise essas variáveis em relação às coordenadas dos outros pontos. Por exemplo, se `THT` (ponta do polegar) estiver acima de `THM` (metacarpo do polegar), isso indica que o polegar está levantado. Da mesma forma, você pode analisar as outras variáveis para determinar a posição dos outros dedos. Essa lógica é utilizada para contar os dedos levantados no script.

# Cálculo da Quantidade de Dedos Levantados

No trecho de código abaixo, o script realiza a comparação correta entre as coordenadas dos pontos-chave dos dedos para determinar se um dedo está levantado. Essa lógica é usada para contar a quantidade de dedos levantados.

```python
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
```

**Explicação:**
- A condição `THT > THM` verifica se a ponta do polegar (`THT`) está acima do metacarpo do polegar (`THM`). Se verdadeiro, incrementa a variável `dedos_levantados` em 1.
- As condições semelhantes para os outros dedos seguem a mesma lógica. Elas comparam as coordenadas y das pontas dos dedos com as coordenadas y das articulações intermediárias, verificando se a ponta do dedo está acima da articulação.
- A variável `dedos_levantados` acumula a quantidade total de dedos levantados.
- Por fim, o número total de dedos levantados é exibido na tela usando a função `cv2.putText`.

Essa abordagem é utilizada para determinar a posição dos dedos e fornecer um feedback visual da quantidade de dedos levantados na interface gráfica.

## Funcionalidades

O script realiza a detecção de mãos em tempo real e exibe a quantidade de dedos levantados na interface gráfica. Além da contagem de dedos, o projeto implementa funcionalidades específicas dependendo do dedo levantado após precionar a tecla "g":

1. **Dedão (polegar): Abrir Calculadora em Python**
   - Ao levantar o dedão, o sistema executará uma calculadora em Python, proporcionando uma experiência rápida e eficiente para cálculos.

2. **Indicador: Abrir Notepad**
   - Levantando o indicador, o sistema abrirá o Notepad, oferecendo um acesso fácil para tomar notas ou fazer edições de texto simples.

3. **Dedo Médio: Minimizar Todas as Janelas (Win + D)**
   - Levantar o dedo médio executará o comando para minimizar todas as janelas ativas, proporcionando uma maneira rápida de organizar a área de trabalho.

4. **Anelar: Capturar Tela (Print Screen)**
   - Ao levantar o dedo anelar, o sistema realizará uma captura de tela, permitindo capturar e salvar a visualização atual da tela para referência ou compartilhamento.

5. **Mindinho: Abrir Explorador de Arquivos (Win + E)**
   - Levantar o mindinho executará o comando para abrir o Explorador de Arquivos, proporcionando um acesso rápido e conveniente para navegar pelos arquivos do sistema.

## Layout dos IDs

Os IDs de cada parte do dedo:
![image](https://github.com/Braian555/HandTrackify/assets/76633571/c6802274-998d-4933-a7c6-40f506a8f606)


## Contribuição

Você está convidado a contribuir com melhorias ou correções. Abra uma issue ou envie um pull request de acordo com os termos da [LICENSE](https://github.com/Braian555/HandTrackify/blob/main/LICENSE).

## Licença

Este projeto está licenciado sob os termos da [LICENSE](https://github.com/Braian555/HandTrackify/blob/main/LICENSE).

Para uma compreensão mais aprofundada do código, consulte o script `hand_command.py` que contém a lógica principal de detecção de gestos.
