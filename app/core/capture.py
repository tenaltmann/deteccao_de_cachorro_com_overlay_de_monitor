import mss                  # Biblioteca para captura de tela
import numpy as np          # Biblioteca para manipulação de arrays (imagens) / transforma a imagem da tela em uma matriz de pixels


class ScreenCapture:        # Classe responsável por capturar a tela do monitor e fornecer os frames para processamento
    def __init__(self, monitor_index=1):     # Inicializa a captura de tela e define o monitor a ser capturado
        with mss.mss() as sct:
            monitors = sct.monitors
            # mss.monitors[0] representa o desktop virtual; índices >= 1 são monitores reais.
            if monitor_index < 1 or monitor_index >= len(monitors):
                monitor_index = 1
            self.monitor = monitors[monitor_index]
        
        
        #self.sct = mss.mss()    # Abre a captura de tela - o "sct" é o objeto responsável por capturar o monitor    
        #self.monitor = self.sct.monitors[1]  # Captura do monitor principal        0 - seleciona todos os monitores / 1 - seleciona o monitor principal

    def get_frame(self):    # Captura um frame da tela, converte para um array NumPy e retorna para processamento
        with mss.mss() as sct:
            screenshot = sct.grab(self.monitor)
            # converte para numpy
            frame = np.array(screenshot)

            # remove canal alpha (fica só BGR - 3 canais)
            frame = frame[:, :, :3].copy()

            return frame
        
        
        #screenshot = self.sct.grab(self.monitor)  # Gera um screechot do monitor (captura a tela)  # converte o "screenshot" em um array NumPy (matriz de pixels)
        #return np.array(screenshot)     #   # converte o "screenshot" em um array NumPy (matriz de pixels)









