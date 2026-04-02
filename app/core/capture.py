import mss                  # Biblioteca para captura de tela
import numpy as np          # Biblioteca para manipulação de arrays (imagens) / transforma a imagem da tela em uma matriz de pixels


class ScreenCapture:        # Classe responsável por capturar a tela do monitor e fornecer os frames para processamento
    def __init__(self):     # Inicializa a captura de tela e define o monitor a ser capturado
        self.sct = mss.mss()    # Abre a captura de tela - o "sct" é o objeto responsável por capturar o monitor    
        self.monitor = self.sct.monitors[1]  # Captura do monitor principal        0 - seleciona todos os monitores / 1 - seleciona o monitor principal

    def get_frame(self):    # Captura um frame da tela, converte para um array NumPy e retorna para processamento
        screenshot = self.sct.grab(self.monitor)  # Gera um screechot do monitor (captura a tela)  # converte o "screenshot" em um array NumPy (matriz de pixels)
        return np.array(screenshot)     #   # converte o "screenshot" em um array NumPy (matriz de pixels)









