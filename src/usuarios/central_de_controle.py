import sys
import os
import numpy as np
import cv2
import torch.nn.functional as F
import torch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.utility.arquivos import manipulador_de_arquivo
from src.captar_e_manipular_imagens.capturar_imagens import CapturarImagem
from src.tripletloss.gerar_embeddings import GeradorEmbedding



class central_de_controle():
    def __init__(self):
        self.nome = None
        self.embedding = None
        self.turma = None
        self.presença = None

        self.capture = CapturarImagem()
        self.gerador = GeradorEmbedding()
        self.flag = 0
        
        

    def gerar_embedding_medio(self, media_esperada=10):
        print("Prepare para a fotinho, diga X'ssssss")
        soma = None

        for i in range(media_esperada):
            self.capture.capturar_imagens(1)
            self.embedding = self.gerador.gerar_embedding(
                r"D:\Desktop\IA3\Dataset\Imagens_para_uso_rapido\face_1.jpg"
            )

            
            if isinstance(self.embedding, np.ndarray):
                self.embedding = torch.from_numpy(self.embedding).float()

            if soma is None:
                soma = self.embedding.clone()
            else:
                soma += self.embedding

        embedding_medio = soma / media_esperada

        
        embedding_medio = F.normalize(embedding_medio, p=2, dim=0)

        return embedding_medio



    def adicionar_aluno_com_embedding_medio(self):
        print("Voce deseja addicionar algum aluno?" + "\n" + "1 == SIM" + "\n" + "0 == NÂO")
        self.flag = int(input())
        while self.flag != 1 or self.flag != 0:
            if self.flag == 1:
                print("Digite o nome: "); self.nome = input()
                print("Digite o nome da turma: "); self.turma = input()
                
                print("Agora vamos processar o reconhecimento facial: diga X'sss "); self.embedding = self.gerar_embedding_medio()
                self.embedding.tolist()

                arquivo = manipulador_de_arquivo(self.nome, self.embedding, self.turma, 0)

                arquivo.escrever_arquivo()
                break
            elif self.flag == 0:
                print("Finalizando a sessão....")
                break
            else:
                print("Voce deseja addicionar algum aluno?" + "\n" + "1 == SIM" + "\n" + "0 == NÂO")
                self.flag = int(input())



    def adicionar_aluno(self):
        print("Voce deseja addicionar algum aluno?" + "\n" + "1 == SIM" + "\n" + "0 == NÂO")
        self.flag = int(input())
        while self.flag != 1 or self.flag != 0:
            if self.flag == 1:
                print("Digite o nome: "); self.nome = input()
                print("Digite o nome da turma: "); self.turma = input()
                
                print("Agora vamos processar o reconhecimento facial: diga X'sss "); self.capture.capturar_imagens(1); self.embedding = self.gerador.gerar_embedding(r"D:\Desktop\IA3\Dataset\Imagens_para_uso_rapido\face_1.jpg")

                self.embedding.tolist()

                arquivo = manipulador_de_arquivo(self.nome, self.embedding, self.turma, 0)

                arquivo.escrever_arquivo()
                break
            elif self.flag == 0:
                print("Finalizando a sessão....")
                break
            else:
                print("Voce deseja addicionar algum aluno?" + "\n" + "1 == SIM" + "\n" + "0 == NÂO")
                self.flag = int(input())

    def comparar_embedding(self):
        print("Qual o nome da pessoa que voce deseja pesquisar"); self.nome = input()

        
        arquivo = manipulador_de_arquivo(self.nome, self.embedding, self.turma, 0)

        emb = arquivo.recuperar_embedding_por_nome(self.nome); self.capture.capturar_imagens(1); self.embedding = self.gerador.gerar_embedding(r"D:\Desktop\IA3\Dataset\Imagens_para_uso_rapido\face_1.jpg")

        if emb is not None and self.embedding is not None:
            similaridade = np.dot(emb, self.embedding)
            print(f"Similaridade entre: {similaridade:.4f}")
            return similaridade
        return None
    

    
    def chamada(self): #Lembrete: IMPLEMENTAR A SOMATÓRIA DE PRESENÇAS TOTAIS DOS ALUNOS NA TURMA
        cv2.namedWindow("Chamada", cv2.WINDOW_NORMAL)

        print("Iniciando a chamada, fiquem calados!")
        while True:
            cv2.imshow("Chamada", np.zeros((1, 1, 3), dtype=np.uint8))
            tecla = cv2.waitKey(1) & 0xFF
            
            if tecla == 27:
                print("Fim da chamada, estão liberados!")
                break
            arquivo = manipulador_de_arquivo(self.nome, self.embedding, self.turma, 0); self.capture.capturar_imagens(1); self.embedding = self.gerador.gerar_embedding(r"D:\Desktop\IA3\Dataset\Imagens_para_uso_rapido\face_1.jpg")

            arquivo.comparar_embedding(self.embedding)
        cv2.destroyAllWindows()


        
        

    

    

        