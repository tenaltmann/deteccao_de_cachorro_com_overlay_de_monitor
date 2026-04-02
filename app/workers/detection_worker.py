from PyQt5 import QtCore  # Importa o módulo principal do PyQt para threads e sinais


class DetectionWorker(QtCore.QThread):  
    # Thread responsável por capturar a tela, detectar objetos e enviar os resultados para a interface

    update_boxes = QtCore.pyqtSignal(list)  
    # Sinal que envia uma lista de bounding boxes (coordenadas dos objetos detectados)


    def __init__(self, capture, detector):
        super().__init__()

        self.capture = capture  
        # Instância responsável por capturar os frames da tela

        self.detector = detector  
        # Instância responsável por processar o frame e detectar objetos


    def run(self):  
        # Método executado automaticamente quando a thread é iniciada (worker.start())

        while True:  
            # Loop contínuo para processar frames em tempo real

            frame = self.capture.get_frame()  
            # Captura um frame atual da tela

            boxes = self.detector.detect(frame)  
            # Executa a detecção de objetos no frame
            # Retorna uma lista de bounding boxes (x1, y1, x2, y2)

            self.update_boxes.emit(boxes)  
            # Envia as caixas detectadas para a interface (overlay)
            # O overlay usará esses dados para desenhar os retângulos na tela