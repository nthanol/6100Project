import pandas as pd
from torch.utils.data import Dataset
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler

class HeartDataset(Dataset):
    def __init__(self, fileName):
        csv = pd.read_csv(fileName)
        data = csv.iloc[:,0:13].values
        labels = csv['target'].values

        sc = StandardScaler()
        data = sc.fit_transform(data)

        self.data = torch.tensor(data, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.float32)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        return self.data[index], self.labels[index]

class Classifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(13, 60),
            nn.ReLU(),
            #nn.Dropout(0.2),

            nn.Linear(60, 60),
            nn.ReLU(),
            #nn.Dropout(0.2),
            
            nn.Linear(60, 60),
            nn.ReLU(),
            #nn.Dropout(0.2),

            nn.Linear(60, 50),
            nn.ReLU(),
            #nn.Dropout(0.2),
            

            nn.Linear(50, 1),
        
        )

    def forward(self, x):
        return self.model(x)