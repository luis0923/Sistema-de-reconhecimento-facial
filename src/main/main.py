import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.usuarios.central_de_controle import central_de_controle

class Main:
    def __init__(self):
        self.sistema = central_de_controle()
        self.menu()

    def menu(self): #EU do futuro: Alterar esse menu para SC para ficar mais formalzinho
        while True:
            print("\n===== SISTEMA DE PRESENÇA AUTOMATIZADA =====")
            print("1 - Adicionar aluno (com embedding médio)")
            print("2 - Fazer a chamada")
            print("0 - Sair")
            print("==========================================")

            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida!")
                continue

            if opcao == 1:
                self.sistema.adicionar_aluno_com_embedding_medio()

            elif opcao == 2:
                self.sistema.chamada()

            elif opcao == 0:
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    Main()
