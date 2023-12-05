# Hand Gesture Control Project

Este projeto utiliza a biblioteca Mediapipe e OpenCV para rastrear gestos das mãos e controlar ações no computador, como minimizar janelas e alternar entre aplicativos.

## Requisitos

- Python 3.x
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
   pip install -r requirements.txt
   ```

## Uso

Execute o script Python para iniciar o controle de gestos:

```bash
python hand_gesture_control.py
```

## Configuração

Você pode configurar a resolução da câmera, a confiança da detecção e outros parâmetros no início do arquivo `hand_gesture_control.py`.

## Funcionalidades

- **Minimizar Janelas:** Ao abrir a mão, todas as janelas serão minimizadas pressionando `Win + D`.
- **Alternar entre Aplicativos:** Ao abrir a mão e fechar novamente, alternará entre aplicativos usando `Alt + Tab`.

## Cores dos Círculos

As cores dos círculos desenhados nas mãos podem ser personalizadas no arquivo `handDetector.py`. Modifique os valores RGB para alterar as cores.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou corrigir problemas. Abra uma issue ou envie um pull request!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
