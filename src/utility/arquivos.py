import json
import os
import sys
import numpy as np
import smtplib
from email.mime.text import MIMEText

#Da PARA REDUZIR MUITO CÓDIGO NESSA CLASSE

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.usuarios.pessoa import pessoa

class manipulador_de_arquivo(pessoa):
    def __init__(self, nome, embedding, turma, presença_inicial = 0):
        super().__init__(nome, embedding, turma, presença_inicial)

        self.nome_do_arquivo = "dados_dos_alunos_de_IIA.json"
        self.arquivo_de_presença = "Presenças_de_hoje_dos_alunos_de_IIA"
        self.presenças = False
        self.dados = {
            "nome" : self.get_nome(),
            "embedding": self.get_embedding().tolist() if self.get_embedding() is not None else [],
            "turma" : self.get_turma(),
            "presenças" : self.get_presença()
        }

        self.presenças_hoje = {
            "nome" : self.get_nome(),
            "presenças":  self.presenças
        }

  
    def carregar_arquivo(self): #Da para otimizar todo o código reaproveitando essa função
        if os.path.exists(self.nome_do_arquivo):
            print("Arquivo existente")
        else:
            with open(self.nome_do_arquivo, "w", encoding= "utf-8") as arquivo:
                json.dump(self.dados, arquivo, indent = 4, ensure_ascii= False)

    def carregar_presenças(self):
            with open(self.arquivo_de_presença, "w", encoding= "utf-8") as arquivo:
                json.dump(self.presenças_hoje, arquivo, indent = 4, ensure_ascii = False)

    def anotar_presença(self, pessoa):
        caminho = os.path.abspath(r"D:\Desktop\IA3\Presenças_de_hoje_dos_alunos_de_IIA.json")

        if not os.path.exists(caminho):
            print("A lista ainda não passou, tenha paciência")
            utilidade = []
        else:
            with open(caminho, "r", encoding= "utf-8") as arquivo:
                try:
                    utilidade = json.load(arquivo)
                except json.JSONDecodeError:
                    utilidade = []


        if not isinstance(utilidade, list):
            utilidade = [utilidade]

        nome_atual = pessoa

        for aluno in utilidade:
            if aluno["nome"] == nome_atual:
                aluno["presenças"] = True
                print(f"Aluno {nome_atual} está presente")

                with open(caminho, "w", encoding="utf-8") as arquivo:
                    json.dump(utilidade, arquivo, indent=2, ensure_ascii=False)

                return
        
        utilidade.append({
            "nome": nome_atual,
            "presenças" : True
        })
        print(f"Aluno {nome_atual} está presente")

        with open(caminho, "w", encoding= "utf-8") as arquivos:
            json.dump(utilidade, arquivos, indent = 1, ensure_ascii= False)


    def escrever_arquivo(self):
        if os.path.exists(self.nome_do_arquivo):
            with open(self.nome_do_arquivo, "r", encoding= "utf-8") as arquivo:
                try:
                    dados_existentes = json.load(arquivo)
                except json.JSONDecodeError:
                    dados_existentes = []

        else: dados_existentes = []
        
        if not isinstance(dados_existentes, list):
            dados_existentes = [dados_existentes] 

        dados_existentes.append(self.dados)


        with open(self.nome_do_arquivo, "w", encoding= "utf-8") as arquivos:
            json.dump(dados_existentes, arquivos, indent= 1, ensure_ascii= False)

    def recuperar_embedding_por_nome(self, nome_procurado): #Inutil
        caminho = os.path.abspath(r"D:\Desktop\IA3\dados_dos_alunos_de_IIA.json")

        if not os.path.exists(caminho):
            print("Arquivo não encontrado:", caminho)
            return None

        with open(caminho, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)

        for aluno in alunos:
            if aluno["nome"] == nome_procurado:
                return np.array(aluno["embedding"], dtype=np.float32)

        print("Aluno não encontrado.")
        return None

    def comparar_embedding(self, embedding):
        caminho = os.path.abspath(r"D:\Desktop\IA3\dados_dos_alunos_de_IIA.json")

        if not os.path.exists(caminho):
            print("Arquivo não encontrado: ", caminho)
        
        with open(caminho, "r", encoding= "utf-8") as arquivo:
            emb = json.load(arquivo)

        for emb_procurado in emb:           
            if emb_procurado["embedding"]:
                aluno_atual = emb_procurado["nome"]
                
                a = np.array(emb_procurado["embedding"], dtype=np.float32)
                sim = np.dot(a, embedding) / ((np.linalg.norm(a)) * (np.linalg.norm(embedding)))
                print(sim) #Só válido em carater de teste, depois remova luis ddo futuro
                if sim >= 0.85:
                    self.anotar_presença(aluno_atual)
                    return
            
        print("Não existe esse aluno nesta turma!")
        return None


    def enviar_arquivos(): #retornar
        pass

        


