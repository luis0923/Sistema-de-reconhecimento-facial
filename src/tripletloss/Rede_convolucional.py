import torch
import torch.nn as nn
import torch.nn.functional as F
import dataset




#ANOTAÇõES PARA USO E ENTENDIMENTO
#Camadas Convolucionais (Con layers): núcleo da rede neural, exxtrai as características de uma imagem, como a borda, textura, formas, camadas mais profundas e padrões maix complexos.
#nn.Conv2d(Entrada:3, Saída:64, Filtra por uma matriz 3x3: kernel_size = 3, adiciona uma borda: padding = 1)

#nn.BatchNorm2d(64):Normalizzação por lote(Batch Normalization): Ela estabilizao treinamento e acelera a convergência, ajustando a média e variância dos valores de saida dda convulsão

#nn.ReLU(inplace = True): Ela introduz a não linearidade, o quê é essencial para a rede aprender padroões complexos

#nn.MaxPool2d(kernel_size=2, stride=2):Ela pega blocos de 2×2 e mantém apenas o maior valor de cada bloco.

class Rede_convolucional(nn.Module):
    "Está inutilizada, futuramente gostaria de capacitar uma cnn própria para capacitar"
    def __init__(self, dimensoes_do_embedding = 64):
        super().__init__()

        self.features = nn.Sequential( #Como exemplo da rede CNN
            #Primeira camada
            nn.Conv2d(3, 64, kernel_size= 3, padding= 1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace = True),
            nn.MaxPool2d(kernel_size= 2, stride= 2), #Ser mais agressivo no pooling ou não ser, eis a questão? talvez mais interessante para coisas menos detatlhistas, como gabarito!

            nn.Conv2d(64, 128, kernel_size= 3, padding= 1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace = True),
            nn.MaxPool2d(kernel_size= 2, stride= 2),
            
            nn.Conv2d(128, 256,kernel_size= 3, padding= 1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace = True),
            nn.MaxPool2d(kernel_size= 2, stride= 2),

            
            nn.Conv2d(256, 512, kernel_size= 3, padding= 1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace = True),
            nn.MaxPool2d(kernel_size= 2, stride= 2),

        )


        self.pool_final = nn.AdaptiveAvgPool2d((1, 1))


        self.classificador = nn.Sequential(
    
            nn.Dropout(0.5),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace= True),
            nn.Dropout(0.5), #Apagar menos neuronios?
            nn.Linear(256, dimensoes_do_embedding)
        )
    def forward(self, x):
        x = self.features(x)
        x = self.pool_final(x)
        x = torch.flatten(x, 1)
        x = self.classificador(x)
        # Normalizar os embeddings
        x = F.normalize(x, p=2, dim=1) #aplica o módulo em cada um dos embeddings
        return x


