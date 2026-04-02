#  Projeto Reconhecimento de Alvo em Tela

Sistema de detecção de objetos em tempo real baseado em captura de tela, utilizando YOLO e um overlay transparente para exibição visual diretamente sobre o monitor.

---

## Objetivo

Detectar objetos (ex: pessoas, animais) diretamente a partir da imagem exibida no monitor, sem depender de integração direta com câmeras ou softwares externos.

O sistema permite:

* Captura da tela em tempo real
* Detecção de objetos com YOLO
* Desenho de bounding boxes sobre a tela
* Base para eventos (ex: cruzamento de linha, alertas)

---

##  Arquitetura do Projeto

O sistema é dividido em módulos independentes, seguindo boas práticas de separação de responsabilidades.

```text
Projeto_reconhece_alvo/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── capture.py
│   │   ├── detector.py
│   │
│   ├── overlay/
│   │   ├── overlay.py
│   │
│   ├── workers/
│   │   ├── detection_worker.py
│
├── models/
│   └── yolov8n.pt
│
├── requirements.txt
└── README.md
```

---

## 📂 Estrutura e Responsabilidades

###  `app/main.py`

Orquestrador da aplicação.

Responsável por:

* Inicializar a aplicação PyQt
* Instanciar os componentes principais
* Conectar sinais e slots
* Iniciar a thread de detecção

 Não contém lógica de negócio — apenas coordenação.

---

###  `core/capture.py`

Captura da tela.

Responsável por:

* Capturar frames do monitor usando MSS
* Converter os dados em formato utilizável (NumPy array)

👉 Entrada do sistema (fonte de dados).

---

###  `core/detector.py`

Detecção de objetos.

Responsável por:

* Carregar o modelo YOLO
* Processar frames
* Retornar bounding boxes (x1, y1, x2, y2)

 Cérebro do sistema.

---

###  `overlay/overlay.py`

Interface gráfica (overlay).

Responsável por:

* Criar uma janela transparente sobre a tela
* Desenhar bounding boxes
* Atualizar visualmente os objetos detectados

 Camada de visualização.

---

###  `workers/detection_worker.py`

Thread de processamento.

Responsável por:

* Executar captura e detecção em loop contínuo
* Rodar em paralelo à interface gráfica
* Emitir sinais com os resultados (bounding boxes)

 Motor do sistema.

---

###  `models/yolov8n.pt`

Modelo de detecção.

* Versão leve do YOLO (Ultralytics)
* Responsável pela identificação dos objetos

---

###  `requirements.txt`

Lista de dependências do projeto.

Exemplo:

```
ultralytics
opencv-python
numpy
mss
PyQt5
```

---

##  Fluxo de Execução

```text
[ScreenCapture]
      ↓
captura frame
      ↓
[DetectionWorker]
      ↓
envia frame para
      ↓
[Detector (YOLO)]
      ↓
retorna bounding boxes
      ↓
(emite sinal)
      ↓
[Overlay]
      ↓
desenha na tela
```

---

##  Execução Assíncrona

A detecção roda em uma thread separada (`DetectionWorker`), garantindo:

* Interface fluida
* Processamento contínuo
* Melhor desempenho

Comunicação entre thread e interface é feita via **signals/slots do PyQt**.

---

##  Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o projeto:

```bash
python app/main.py
```

---

##  Próximos Passos

* Detecção de cruzamento de linha (eventos)
* Sistema de alertas (log, som, API)
* Otimização de performance (GPU / batch)
* Suporte a múltiplos monitores

---

##  Conceitos Utilizados

* Computer Vision
* Object Detection (YOLO)
* Multithreading
* Overlay gráfico em tempo real
* Arquitetura modular

---

##  Autor

Projeto desenvolvido para fins de estudo e evolução em visão computacional e engenharia de software.
