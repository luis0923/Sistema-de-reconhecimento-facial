import torch
from torch.utils.data import DataLoader
from tripletdataset import triplet_data_set
from rede_resnet import Rede_convolucional
import torch.nn as nn
from checkpoint import checkpoint  
from dataloader import Data_loader
import torch.nn.functional as F
import numpy as np

class Treinamento:

    def treinar(self):

        loader = Data_loader().data_loader



        device = torch.device("cpu") #utilizar da CPU

        rede = Rede_convolucional().to(device)

        criterio = nn.TripletMarginLoss(margin=0.2, p=2)                               #Responsável por aplicar a formula L=max(d(A,P)−d(A,N)+α,0)
        otimizador = torch.optim.Adam(rede.parameters(), lr=1e-5)


        epoca_inicial = 0
        total_epocas = 120

        ckpt = checkpoint(r"D:\Desktop\IA3\modelo_triplet2.pth")
        
        best_loss = float("inf")

        try:
            epoca_inicial, best_loss = ckpt.carregar_checkpoint(rede, otimizador)
            print(f"Iniciando a partir da época {epoca_inicial + 1}")
        except:
            print("Nenhum checkpoint encontrado. Iniciando do zero.")


        rede.train() #Treino! entra em modo treino, então os pesos acabam sendo subjetivos e aleatórios
 

        for epoca in range(epoca_inicial, total_epocas):

            perdas_por_epoca = 0.0

            for anchor, positive, negative in loader:

                anchor = anchor.to(device)
                positive = positive.to(device)
                negative = negative.to(device)


                otimizador.zero_grad()

                emb_a = rede(anchor)
                emb_p = rede(positive)
                emb_n = rede(negative)
                
                #Normalize esse carai
                emb_a = F.normalize(emb_a, p=2, dim=1)
                emb_p = F.normalize(emb_p, p=2, dim=1)
                emb_n = F.normalize(emb_n, p=2, dim=1)

                sim1 = F.cosine_similarity(emb_a, emb_p, dim=1).mean().item()

                sim2 = F.cosine_similarity(emb_a, emb_n, dim=1).mean().item()
                #Remover depois? talvez!

                print("Similaridade AP: ", sim1)
                print("Similariade AN: ", sim2)

                loss = criterio(emb_a, emb_p, emb_n)

                loss.backward()
                otimizador.step()

                perdas_por_epoca += loss.item()

            print(f"Época {epoca+1}/{total_epocas} | Loss total: {perdas_por_epoca:.4f}")


            if perdas_por_epoca < best_loss:
                best_loss = perdas_por_epoca
                ckpt.salvar_checkpoint(rede, otimizador, epoca, best_loss)
                print(">>> Novo melhor modelo salvo!")

        print("\nTreinamento concluído!")


if __name__ == '__main__':
    treino = Treinamento()
    treino.treinar()
