# Sistema de reconhecimento facial (Readme Generico, tudo vai melhorar)

**1. Descrição do Projeto**

Este projeto implementa um sistema de reconhecimento facial utilizando aprendizado profundo, extração de embeddings, Triplet Loss e uma arquitetura baseada em ResNet.
O objetivo é mapear rostos para um espaço vetorial onde imagens da mesma pessoa ficam próximas, e imagens de pessoas diferentes ficam distantes.
O sistema permite verificação, identificação e comparação facial.


**2. Tecnologias Utilizadas**

Ambiente:

Python 3.11.2

Bibliotecas principais:

PyTorch

Torchvision

NumPy

OpenCV (cv2)

InsightFace (FaceAnalysis)

**3. Dataset Utilizado**

O modelo foi treinado com o dataset LFW – Labeled Faces in the Wild, um conjunto amplamente utilizado para pesquisas de reconhecimento facial em ambientes não controlados.

Referência oficial:

Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments
http://vis-www.cs.umass.edu/lfw/

**Observações:**
**-O dataset não está incluído neste repositório.**
**-O download deve ser feito diretamente pelo site oficial.**

**4. Ausência do Modelo Treinado (Checkpoint)**

O arquivo de pesos treinados (modelo_triplet2.pth) não está incluído no repositório.
O motivo é que o GitHub possui limite de 100 MB por arquivo, e o checkpoint final possui aproximadamente 130 MB, excedendo esse limite.

Caso seja necessário, o modelo pode ser disponibilizado (Drive)(provavelmente vai estar mas não hoje rsrs).

**5. Como Treinar o Modelo**

Baixe e extraia o dataset LFW.

Organize o dataset no formato: 
dataset/
    pessoa1/
        img1.jpg
        img2.jpg ...
    pessoa2/
        img1.jpg
        img2.jpg ...
    ...

  ** Projeto desenvolvido por:**
Luís Augusto Bezerra Campos
aplicações de conceitos de visão computacional, reconhecimento facial e deep learning.

