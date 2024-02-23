# from glob import glob
# from os import getcwd
# import json
# import csv

# # with open("./sets/hiragana.json") as f:
# #     # print(json.load(f))
# #     for i in json.load(f):
# #         lol = glob(f"{getcwd()}/ETL9B_CONVERTED/{i}")
# #         print(lol)

# xyz_info = ["id", "data_1", "data_2"]
# xyz = [
#     [1, 0.324, "eyy"],
#     [2, 0.432, "wdaw"],
#     [3, 0.5765, "21312"],
# ]

# with open("./csv_test.csv", "w", newline="") as f:
#     f.write("sep=;\n")
#     writer = csv.writer(f, delimiter=";")
#     writer.writerow(xyz_info)
#     writer.writerows(xyz)

# with open("./csv_test.csv", "r") as f:
#     reader = csv.reader(f, delimiter=";")

#     for row in reader:
#         print(row)

# import torch

# torch.load("dataset.pt")

# import PIL

# img = PIL.open("C:\\Users\\imasl\\Downloads\\etlcdb-image-extractor\\images\\ETL7\\0x305b\\002624.png")

# import torch
# from torch import nn
# from torch.utils.data import DataLoader, random_split
# from tqdm import tqdm


# class CNN_8(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv = lambda x, y, z: nn.Conv2d(x, y, z)
#         self.conv1 = nn.Conv2d(1, 64, 3)
#         self.conv2 = nn.Conv2d(64, 128, 3)
#         self.conv3 = nn.Conv2d(128, 256, 3)
#         self.conv4 = nn.Conv2d(256, 512, 5)
#         self.act = nn.ReLU()
#         self.drop1 = nn.Dropout(0.2)
#         self.drop2 = nn.Dropout(0.4)
#         self.pool = nn.MaxPool2d(2)
#         self.flat = nn.Flatten()
#         self.hidden = lambda x, y: nn.Linear(x, y)
#         self.hidden1 = nn.Linear(512, 1024)
#         self.hidden2 = nn.Linear(1024, 3036)

#     def forward(self, x):
#         x = self.pool(self.drop1(self.act(self.conv1(x))))
#         # print(x.size())
#         x = self.pool(self.drop2(self.act(self.conv2(x))))
#         x = self.pool(self.drop2(self.act(self.conv3(x))))
#         x = self.pool(self.drop2(self.act(self.conv4(x))))
#         # x = self.flat(x)
#         # print(x.size())
#         x = x.view(-1, 512)
#         # print(x.size())
#         x = self.act(self.hidden1(x))
#         # print(x.size())
#         x = self.hidden2(x)
#         return x


# dataset = torch.load("dataset-custom.pt")

# _, test_set = random_split(dataset, [0.9, 0.1])
# test_loader = DataLoader(test_set, 16, True)
# device = torch.device("cpu")

# with torch.no_grad():
#     test_correct = 0

#     best_model = CNN_8()
#     # best_model.cuda()
#     best_model.load_state_dict(torch.load("model_3_8.pt"))
#     # best_model.load_state_dict(torch.load(f"{CUSTOM_MODEL_PATH}.pt"))
#     best_model.eval()
#     for x, y in tqdm(test_loader):
#         (x, y) = x.to(device), y.to(device)
#         pred = best_model(x)
#         test_correct += (pred.argmax(1) == y).type(torch.float).sum().item()

# test_acc = test_correct / len(test_set)
# print(f"test accuracy: {test_correct / len(test_set)}")

# import torch
# import utils
# import json

# # dataset = classes.CustomDataset(dataframe)
# # dataset = torch.load("./dataset-hiragana.pt")
# # torch.save(dataset, "dataset-katakana-custom.pt")
# labels = json.load(open("./model_3_8.json", "r"))
# labels = list(labels.values())
# labels = [utils.encode_codepoint(label) for label in labels]
# with open("./sets/ETL9B.json", "w+") as f:
#     f.write(json.dumps(labels))


# from PIL import Image, ImageDraw, ImageFont
# import os
# import glob
# import random
# from tqdm import tqdm
# from utils import create_folder, encode_codepoint, decode_codepoint
# from uuid import uuid4
# import json
# from torchvision.transforms import v2

# IMAGES_PER_FONT = 3
# TRANSFORMS_PER_IMAGE = 10
# IMAGES_PER_CHARACTER = 201

# output_path = "CUSTOM_TEST"
# # characters_list = json.load(open("kanjidic2/jouyou_kanji_literals.json"))
# # characters_list = [decode_codepoint(i) for i in json.load(open("sets/katakana.json"))]
# characters_list = [decode_codepoint(i) for i in json.load(open("sets/ETL9B.json"))]
# # characters_list = [decode_codepoint(i) for i in json.load(open("sets/katakana.json"))]
# font_types = []

# create_folder(output_path)

# for font in glob.glob(f"{os.getcwd()}/fonts/*"):
#     font_types.append(os.path.abspath(font))

# for index, fontType in enumerate(font_types):
#     print(f"index {index}\n{fontType}")

# for index, character in enumerate(tqdm(characters_list)):
#     count = 0
#     # for index, character in enumerate(tqdm(characters_list[0])):
#     path = os.path.join(output_path, encode_codepoint(character))

#     create_folder(path)

#     for font_index, font in enumerate(font_types):
#         for image_index in range(IMAGES_PER_FONT):  # Number of Images
#             fnt = ImageFont.truetype(fontType, 50)  # 56
#             img_w, img_h = (64, len(characters_list) * 64)  # 64/64
#             img = Image.new("L", (img_w, img_h), color="black")
#             d = ImageDraw.Draw(img)
#             _, _, w, h = d.textbbox((0, 12), character, font=fnt)
#             d.text(
#                 (
#                     (img_w - w) - 7,
#                     (img_h - h) + 2,
#                 ),
#                 character,
#                 font=fnt,
#                 fill=255,
#                 align="center",
#             )  # TO ALIGN CHARACTER IN CENTER

#             for transform_index in range(TRANSFORMS_PER_IMAGE):
#                 transforms = v2.Compose(
#                     [
#                         v2.RandomPerspective(distortion_scale=0.15, p=0.5),
#                         v2.RandomRotation(degrees=(-2, 2)),
#                         v2.ElasticTransform(alpha=200, sigma=10),
#                         v2.RandomAffine(
#                             degrees=(-2, 2), translate=(0.01, 0.06), scale=(0.98, 1.02)
#                         ),
#                     ]
#                 )
#                 transformed_img = transforms(img)
#                 transformed_img.save(f"{path}/{uuid4()}.png")
#                 count += 1

#                 if count >= IMAGES_PER_CHARACTER:
#                     break
#             if count >= IMAGES_PER_CHARACTER:
#                 break
#         if count >= IMAGES_PER_CHARACTER:
#             break


# import unicodedata
# import os

# fonts = []

# for root, dirs, files in os.walk("./fonts/"):
#     for file in files:
#         if file.endswith(".ttf"):
#             fonts.append(os.path.join(root, file))


# from fontTools.ttLib import TTFont


# def char_in_font(unicode_char, font):
#     for cmap in font["cmap"].tables:
#         if cmap.isUnicode():
#             if ord(unicode_char) in cmap.cmap:
#                 return True
#     return False


# def test(char):
#     for fontpath in fonts:
#         font = TTFont(fontpath)  # specify the path to the font in question
#         if char_in_font(char, font):
#             print(char + " " + unicodedata.name(char) + " in " + fontpath)


# test("飴")

import utils
import json
# utils.format_drawings("hiragana-mouse", "hiragana_mouse_drawn")

etl9b = json.load(open("sets/ETL9B.json"))
hiragana = json.load(open("sets/hiragana.json"))
hiragana = [literal.lower() for literal in hiragana]

literals = []
for literal in etl9b:
    if literal.lower() not in hiragana:
        literals.append(literal)

print(len(literals))

with open("./sets/ETL9B_wo_hiragana.json", "w") as f:
    f.write(json.dumps(literals))
