import os
import random
from PIL import Image
import torchvision.transforms as transforms

class Data_set:
    def __init__(self, dataset_path=r"D:\Desktop\new_data_set"):
        self.dataset_path = dataset_path
        
        
        self.todas_pessoas = [p for p in os.listdir(dataset_path) 
                             if os.path.isdir(os.path.join(dataset_path, p))]
        
        print(f"Dataset carregado com {len(self.todas_pessoas)} pessoas") #Nem necessita saber quantas pessoas tem, tirar depois
        
        self.pick_anchor_pessoa = None
        self.pick_positive_pessoa = None  
        self.pick_negative_pessoa = None

        self.pick_anchor_img = None
        self.pick_positive_img = None
        self.pick_negative_img = None

        self.transform = transforms.Compose([
            transforms.Resize((250, 250)),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.5, 0.5, 0.5],
                [0.5, 0.5, 0.5]
            )
        ])

    def picks(self):
        
        self.pick_anchor_pessoa = random.choice(self.todas_pessoas)
        self.pick_positive_pessoa = self.pick_anchor_pessoa  
        
       
        outras_pessoas = [p for p in self.todas_pessoas if p != self.pick_anchor_pessoa]
        self.pick_negative_pessoa = random.choice(outras_pessoas)
        
       
        arquivos_anchor = os.listdir(os.path.join(self.dataset_path, self.pick_anchor_pessoa))
        arquivos_negative = os.listdir(os.path.join(self.dataset_path, self.pick_negative_pessoa))
        
        
        self.pick_anchor_img, self.pick_positive_img = random.sample(arquivos_anchor, 2)
        self.pick_negative_img = random.choice(arquivos_negative)

    def load_image(self, filename, pessoa):
        path = os.path.join(self.dataset_path, pessoa, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Arquivo não encontrado: {path}")

        img = Image.open(path).convert("RGB")
        return self.transform(img)

    def get_triplet(self):
        
        self.picks()
        
        anchor = self.load_image(self.pick_anchor_img, self.pick_anchor_pessoa)
        positive = self.load_image(self.pick_positive_img, self.pick_positive_pessoa)
        negative = self.load_image(self.pick_negative_img, self.pick_negative_pessoa)
        
        return anchor, positive, negative