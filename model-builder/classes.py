from pandas import DataFrame
from torch.utils.data import Dataset
from torchvision import transforms
import torch.nn as nn
from collections import Counter
from consts import CLASSES_COUNT
# from torchvision.io import read_image


class Custom_dataset(Dataset):
    def __init__(self, df: DataFrame):
        self.tensors = df["image"].to_list()
        self.labels = df["literal"].to_list()
        self.unique_labels = list(Counter(self.labels).keys())

    def __len__(self):
        return len(self.tensors)

    def __getitem__(self, index):
        return self.tensors[index], self.unique_labels.index(self.labels[index])

    def adjust(self, trained_dataset_map: dict):
        trained_unique_labels = trained_dataset_map.items()
        for i in range(len(self.labels)):
            if self.labels[i] not in trained_unique_labels:
                self.tensors[i] = None
                self.labels[i] = None
        self.tensors = list(filter(lambda x: x is not None, self.tensors))
        self.labels = list(filter(lambda y: y is not None, self.labels))
        self.unique_labels = trained_unique_labels


class CNN_1(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 32, 3)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.act = nn.ReLU()
        self.drop = nn.Dropout(0.5)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(4608, 1024)
        self.hidden2 = nn.Linear(1024, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop(self.act(self.conv2(x))))
        x = self.pool(self.drop(self.act(self.conv3(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 4608)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


class CNN_2(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 64, 3)
        self.conv2 = nn.Conv2d(64, 128, 3)
        self.conv3 = nn.Conv2d(128, 256, 3)
        self.conv4 = nn.Conv2d(256, 512, 3)
        self.act = nn.ReLU()
        self.drop = nn.Dropout(0.5)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(2048, 1024)
        self.hidden2 = nn.Linear(1024, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop(self.act(self.conv2(x))))
        x = self.pool(self.drop(self.act(self.conv3(x))))
        x = self.pool(self.drop(self.act(self.conv4(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 2048)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


class CNN_3(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 64, 3)
        self.conv2 = nn.Conv2d(64, 64, 3)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv4 = nn.Conv2d(128, 256, 3)
        self.act = nn.ReLU()
        self.drop = nn.Dropout(0.5)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(3200, 1024)
        self.hidden2 = nn.Linear(1024, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop(self.act(self.conv2(x))))
        x = self.drop(self.act(self.conv2(x)))
        x = self.pool(self.drop(self.act(self.conv3(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 3200)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


class CNN_4(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 64, 7)
        self.conv2 = nn.Conv2d(64, 128, 5)
        self.conv3 = nn.Conv2d(128, 256, 3)
        self.act = nn.ReLU()
        self.drop = nn.Dropout(0.5)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(6400, 1024)
        self.hidden2 = nn.Linear(1024, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop(self.act(self.conv2(x))))
        x = self.pool(self.drop(self.act(self.conv3(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 6400)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


class CNN_5(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 64, 3)
        self.conv2 = nn.Conv2d(64, 128, 3)
        self.conv3 = nn.Conv2d(128, 256, 3)
        self.conv4 = nn.Conv2d(256, 512, 3)
        self.conv5 = nn.Conv2d(512, 1024, 3)
        self.act = nn.ReLU()
        self.drop = nn.Dropout(0.5)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(1024, 1024)
        self.hidden2 = nn.Linear(1024, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop(self.act(self.conv2(x))))
        x = self.drop(self.act(self.conv3(x)))
        x = self.pool(self.drop(self.act(self.conv4(x))))
        x = self.pool(self.drop(self.act(self.conv5(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 1024)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


class CNN_6(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 64, 5)
        self.conv2 = nn.Conv2d(64, 128, 5)
        self.conv3 = nn.Conv2d(128, 256, 3)
        self.conv4 = nn.Conv2d(256, 512, 3)
        self.act = nn.ReLU()
        self.drop = nn.Dropout(0.5)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(512, 1024)
        self.hidden2 = nn.Linear(1024, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop(self.act(self.conv2(x))))
        x = self.pool(self.drop(self.act(self.conv3(x))))
        x = self.pool(self.drop(self.act(self.conv4(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 512)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


class CNN_7(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.conv2 = nn.Conv2d(32, 64, 5)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv4 = nn.Conv2d(128, 256, 3)
        self.conv5 = nn.Conv2d(256, 512, 3)
        self.act = nn.ReLU()
        self.drop = nn.Dropout(0.5)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(512, 1024)
        self.hidden2 = nn.Linear(1024, CLASSES_COUNT)

    def forward(self, x):
        x = self.pool(self.drop(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop(self.act(self.conv2(x))))
        x = self.pool(self.drop(self.act(self.conv3(x))))
        x = self.pool(self.drop(self.act(self.conv4(x))))
        x = self.pool(self.drop(self.act(self.conv5(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 512)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


class CNN_8(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
        self.conv1 = nn.Conv2d(1, 64, 3)
        self.conv2 = nn.Conv2d(64, 128, 3)
        self.conv3 = nn.Conv2d(128, 256, 3)
        self.conv4 = nn.Conv2d(256, 512, 5)
        self.act = nn.ReLU()
        self.drop1 = nn.Dropout(0.2)
        self.drop2 = nn.Dropout(0.4)
        self.pool = nn.MaxPool2d(2)
        self.flat = nn.Flatten()
        self.hidden = lambda x, y: nn.Linear(x, y)
        self.hidden1 = nn.Linear(512, 1024)
        self.hidden2 = nn.Linear(1024, 3036)

    def forward(self, x):
        x = self.pool(self.drop1(self.act(self.conv1(x))))
        # print(x.size())
        x = self.pool(self.drop2(self.act(self.conv2(x))))
        x = self.pool(self.drop2(self.act(self.conv3(x))))
        x = self.pool(self.drop2(self.act(self.conv4(x))))
        # x = self.flat(x)
        # print(x.size())
        x = x.view(-1, 512)
        # print(x.size())
        x = self.act(self.hidden1(x))
        # print(x.size())
        x = self.hidden2(x)
        return x


# class BasicNetwork2(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
#         self.conv1 = nn.Conv2d(1, 32, 3)
#         self.conv2 = nn.Conv2d(32, 64, 3)
#         self.conv3 = nn.Conv2d(64, 128, 3)
#         self.act1 = nn.ReLU()
#         self.act2 = nn.Softmax()
#         self.drop = nn.Dropout(0.5)
#         self.pool = nn.MaxPool2d(2)
#         self.flat = nn.Flatten()
#         self.hidden = lambda x, y: nn.Linear(x, y)
#         self.hidden1 = nn.Linear(4608, 1024)
#         self.hidden2 = nn.Linear(1024, 1024)
#         self.hidden3 = nn.Linear(1024, CLASSES_COUNT)

#     def forward(self, x):
#         x = self.pool(self.drop(self.act(self.conv1(x))))
#         # print(x.size())
#         x = self.pool(self.drop(self.act(self.conv2(x))))
#         x = self.pool(self.drop(self.act(self.conv3(x))))
#         # x = self.flat(x)
#         # print(x.size())
#         x = x.view(-1, 4608)
#         # print(x.size())
#         x = self.act(self.hidden1(x))
#         # print(x.size())
#         x = self.act(self.hidden2(x))
#         x = self.hidden3(x)
#         return x
