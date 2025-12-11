import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F



class Rede_convolucional(nn.Module):
    def __init__(self, dimensoes_do_embedding=128, congelar_backbone=False):
        super().__init__()
        
       
        self.backbone = models.resnet18(pretrained=True)
        
        if congelar_backbone:
            
            for param in self.backbone.parameters():
                param.requires_grad = False
            print("Backbone congelado (frioo) - apenas embedding head treinável")
        
        
        self.backbone.fc = nn.Identity()
        
        
        self.embedding_head = nn.Sequential(
            nn.Dropout(0.5), #Desliga aleatoriamente os neuronios
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3), #De novo
            nn.Linear(256, dimensoes_do_embedding)
        )
        
    def forward(self, x):
        
        features = self.backbone(x)
        
        embedding = self.embedding_head(features)
        
        embedding = F.normalize(embedding, p=2, dim=1)
        return embedding