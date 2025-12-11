from torch.utils.data import Dataset
from dataset import Data_set

class triplet_data_set(Dataset):
    def __init__(self):
        self.ds = Data_set() 
        self.length = 2000    
        
    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        
        anchor, positive, negative = self.ds.get_triplet()
        return anchor, positive, negative