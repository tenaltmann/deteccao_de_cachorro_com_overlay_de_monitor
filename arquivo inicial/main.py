import cv2      # Bibvlioteca de manipulação de video - Irá desenhar o retangulo nos objetos

import numpy as np      # transforma os pixels capturados em um array

from ultralytics import YOLO        # Usado para detectar o item / individuo na imagem

import mss      # faz o screen capture do monitor, para poder reconhecer o que for transmitido no monitor, e posteriormente o aplicativo da camera


model = YOLO("yolov8n.pt")          # Carrega a versão leve do modelo pré-treinado


cv2.namedWindow("Deteccao na Tela", cv2.WINDOW_NORMAL)      #---------------------------------
cv2.resizeWindow("Deteccao na Tela", 800, 600)


with mss.mss() as sct:              # Abre a captura de tela - o "sct" é o objeto responsável por capturar o monitor

    monitor = sct.monitors[1]       # informa qual o monitor sera utilizado para a captura
                                    #           0 - seleciona todos os monitores
                                    #           1 - seleciona o monitor principal

    

    while True:                     # cria o lopp que ira capturar e processar os frames de forma continua

        screenshot = sct.grab(monitor)      # Gera um screechot do monitor (captura a tela)

        frame = np.array(screenshot)        # converte o "screenshot" em um array NumPy (matriz de pixels)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)     # converte o formato da copr de BGRA2 para BGR, pois o OpenCV trabalha com BGR

        #results = model(frame)              # envia o frame para o YOLO e detecta o item / indivíduo
        results = model(frame, verbose=False)   # ---------------------------------

        for r in results:                   # percorre os resultados econtrados

            for box in r.boxes:             # percorre todas as caixas (objetos encontrados)

                cls = int(box.cls[0])       # Obtém a classe ( tipo de ) do objeto encontrado ("Verifica se é cachorro, pessoa, carro, etc.")

                conf = float(box.conf[0])   # obtem a confiança do que foi detectado (0 a 1)

                if cls == 16 and conf > 0.2:
                # se cls for igual a 16 (codigo de cachorro) e conf( confiabilidade da detecção) maior que 0.5 (50% de certeza):

                    x1, y1, x2, y2 = map(int, box.xyxy[0])      # armazena as coordenadas da caixa após a detecção

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)  # imprimi o retangulo na tela em volta do objeto detectado  

                    cv2.putText(                    # estiliza o retangulo e as informações da tela
                        frame,                      # Imagem onde será desenhado
                        "Cachorro",                 # texto
                        (x1, y1-10),                # posição (acima da caixa)
                        cv2.FONT_HERSHEY_SIMPLEX,   # defini a fonte do texto
                        0.7,                        # tamanho da fonte
                        (0,255,0),                  # cor (verde)
                        2                           # Expessura do retangulo
                    )


        cv2.imshow("Deteccao na Tela", frame)      # exibe a imagem com as detecções na tela


        if cv2.waitKey(30) == 27:      #---------------              # encerra o loop se a tecla que contém o codigo "27" (ESC) for pressionada 
            break

cv2.destroyAllWindows()         # Fecha todas as janelas abertas pelo OpenCV

