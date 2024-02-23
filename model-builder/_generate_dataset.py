from PIL import Image, ImageDraw, ImageFont
import os
import glob
import random
from tqdm import tqdm
from utils import create_folder, encode_codepoint, display_image
from torchvision.io import read_image, ImageReadMode
from torchvision.transforms.functional import convert_image_dtype
import torch
from uuid import uuid4
import json
from torchvision.transforms import v2

IMAGES_PER_FONT = 1
TRANSFORMS_PER_IMAGE = 5
# IMAGES_PER_CHARACTER = 201

output_path = "CUSTOM_TEST"
characters_list = json.load(open("kanjidic2/jouyou_kanji_literals.json"))
# characters_list = [decode_codepoint(i) for i in json.load(open("sets/katakana.json"))]
# characters_list = [
#     decode_codepoint(i) for i in json.load(open("sets/ETL9B_wo_hiragana.json"))
# ]
# characters_list = [decode_codepoint(i) for i in json.load(open("sets/katakana.json"))]
font_types = []

create_folder(output_path)

for font in glob.glob(f"{os.getcwd()}/fonts_44/*"):
    font_types.append(os.path.abspath(font))

for index, fontType in enumerate(font_types):
    print(f"index {index}\n{fontType}")

for index, character in enumerate(tqdm(characters_list[:99])):
    count = 0
    # for index, character in enumerate(tqdm(characters_list[0])):
    path = os.path.join(output_path, encode_codepoint(character))

    create_folder(path)

    example_imgs = []
    # for font_index, font in enumerate(font_types):
    for font_index, font in enumerate(
        [font_types[21], font_types[35], font_types[40], font_types[20], font_types[25]]
    ):
        for image_index in range(IMAGES_PER_FONT):  # Number of Images
            font_size = 56
            w_minus = 0
            h_minus = -8

            fnt = ImageFont.truetype(font, font_size)  # 56
            img_w, img_h = (64, 64)  # 64/64
            img = Image.new("L", (img_w, img_h), color="black")
            d = ImageDraw.Draw(img)
            _, _, w, h = d.textbbox((0, 12), character, font=fnt)
            d.text(
                (
                    (img_w - w) - w_minus,
                    (img_h - h) - h_minus,
                ),
                character,
                font=fnt,
                fill=255,
                align="center",
            )  # TO ALIGN CHARACTER IN CENTER

            for transform_index in range(TRANSFORMS_PER_IMAGE):
                transforms = v2.Compose(
                    [
                        v2.RandomPerspective(distortion_scale=0.15, p=0.5),
                        v2.RandomRotation(degrees=(-2, 2)),
                        v2.ElasticTransform(alpha=200, sigma=10),
                        # v2.RandomAffine(
                        #     degrees=(-2, 2), translate=(0.01, 0.06), scale=(0.98, 1.02)
                        # ),
                    ]
                )
                # transforms = v2.Compose(
                #     [
                #         v2.RandomPerspective(distortion_scale=0.1, p=1),
                #         v2.RandomRotation(degrees=(-2, 2)),
                #         v2.ElasticTransform(alpha=[200, 450], sigma=[10, 15]),
                #         v2.RandomAffine(
                #             degrees=(-2, 2), translate=(0.01, 0.06), scale=(0.98, 1.02)
                #         ),
                #     ]
                # )
                transformed_img = transforms(img)
                p = f"{path}/{uuid4()}.png"
                transformed_img.save(p)
                example_imgs.append(
                    convert_image_dtype(
                        read_image(p, ImageReadMode.GRAY), dtype=torch.float
                    )
                )
                count += 1
                break
            break

        if len(example_imgs) == 5:
            display_image(example_imgs, [])
        #         if count >= IMAGES_PER_CHARACTER:
        #             break
        #     if count >= IMAGES_PER_CHARACTER:
        #         break
        # if count >= IMAGES_PER_CHARACTER:
        #     break
