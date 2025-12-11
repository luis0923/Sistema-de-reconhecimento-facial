import torch
from torchvision import transforms
from PIL import Image  # IMPORTAR AQUI
import numpy as np
from src.tripletloss.rede_resnet import Rede_convolucional

class GeradorEmbedding:
    def __init__(self, caminho_checkpoint=r"D:\Desktop\IA3\modelo_triplet2.pth"):
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Usando dispositivo: {self.device}")
        
        # Carregar rede resnet (deu bom)
        self.modelo = Rede_convolucional().to(self.device)
        
        # Carregar checkpoint
        try:
            checkpoint_data = torch.load(caminho_checkpoint, map_location=self.device)
            if "model_state" in checkpoint_data:
                self.modelo.load_state_dict(checkpoint_data["model_state"])
                print("Checkpoint turtututu!")
            else:
                print("Checkpoint falhou tururu, a estrutura é inválida")
                return
        except Exception as e:
            print(f"Erro ao carregar checkpoint: {e}")
            return
        
        self.modelo.eval()
        print("Modo de inferimento ativado")

        
        self.transformacao = transforms.Compose([
            transforms.Resize((250, 250)),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

    def gerar_embedding(self, caminho_imagem):
        try:
            
            img = Image.open(caminho_imagem).convert("RGB")
            
            tensor = self.transformacao(img).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                embedding = self.modelo(tensor)
            
            embedding_np = embedding.cpu().numpy()[0]
            
            
            norma = np.linalg.norm(embedding_np)
            print(f"Norma do embedding: {norma:.6f}") #Se estiver normalizado corretamente,, tem que dar 1.0
            
            return embedding_np
            
        except Exception as e:
            print(f"Erro ao gerar embedding: {e}")
            return None
