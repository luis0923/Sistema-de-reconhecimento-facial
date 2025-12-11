import torch


class checkpoint:


    def __init__(self, caminho = r"D:\Desktop\IA3\modelo_triplet2.pth"):
        self.caminho = caminho

    def salvar_checkpoint(self, modelo, otimizador, epoca, best_loss):
        checkpoint = {
            "epoch": epoca,
            "model_state": modelo.state_dict(),
            "optimizer_state": otimizador.state_dict(),
            "best_loss": best_loss
        }

        torch.save(checkpoint, self.caminho)
        print(f"[CHECKPOINT] turururu {self.caminho}")
        

    def carregar_checkpoint(self, modelo ,otimizador):
        checkpoint = torch.load(self.caminho)

        modelo.load_state_dict(checkpoint["model_state"])
        otimizador.load_state_dict(checkpoint["optimizer_state"])

        epoca = checkpoint["epoch"]
        best_loss = checkpoint["best_loss"]

        print(f"[CHECKPOINT] turururu {epoca+1}")

        return epoca, best_loss