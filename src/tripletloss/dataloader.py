from torch.utils.data import DataLoader
from tripletdataset import triplet_data_set


class Data_loader:
    def __init__(self):
        self.triplet_ds = triplet_data_set()

        self.data_loader = DataLoader(
            self.triplet_ds, 
            batch_size=8, #Quantidades de lotes em que o triplet vai ser dividido em cada epoca
            shuffle=True,
            num_workers=2, #Paralelização, por enquanto duas paralelizações época
            )



