from pandas import DataFrame
from torch.utils.data import Dataset
from torchvision import transforms
import torch.nn as nn
from collections import Counter
from consts import CLASSES_COUNT
# from torchvision.io import read_image


class KanjiDataset(Dataset):
    def __init__(self, df: DataFrame, transform=False):
        self.tensors = df["image"].to_list()
        self.labels = df["literal"].to_list()
        self.unique_labels = list(Counter(self.labels).keys())
        self.transform = transform

    def __len__(self):
        return len(self.tensors)

    def __getitem__(self, index):
        out = transforms.Compose(
            [
                # transforms.CenterCrop(10),
            ]
        )
        tensor = out(self.tensors[index])
        return tensor, self.unique_labels.index(self.labels[index])
        # return tensor, self.labels[index]


class BasicNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 32, 17)
        self.conv2 = nn.Conv2d(32, 64, 5)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.act1 = nn.ReLU()
        self.act2 = nn.Softmax()
        self.drop1 = nn.Dropout(0.4)
        self.drop2 = nn.Dropout(0.2)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(2048, 512)
        self.hidden2 = nn.Linear(512, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop1(self.act1(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop2(self.act1(self.conv2(x))))
        x = self.pool(self.drop2(self.act1(self.conv3(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 2048)
        # print(x.size())
        x = self.act1(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x
