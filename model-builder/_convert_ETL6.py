from glob import glob
from PIL import Image
from uuid import uuid4
from utils import create_folder, encode_codepoint, load_images_paths, load_set
from tqdm import tqdm

PATH_ETL6 = "ETL6"
OUTPUT_PATH = "ETL6_CONVERTED"

if __name__ == "__main__":
    create_folder(OUTPUT_PATH)

    subset = load_set("sets/katakana.json")
    folders = load_images_paths(PATH_ETL6, subset)

    for i in tqdm(folders):
        imgs_in_folder = glob(rf"{i}\*.png")
        unicode = i.split("\\")[-1]
        codepoint = encode_codepoint(unicode)

        create_folder(f"{OUTPUT_PATH}/{unicode}")

        for img_path in imgs_in_folder:
            # resize
            img = Image.open(img_path)
            img.resize((64, 64))
            img.save(f"{OUTPUT_PATH}/{unicode}/{uuid4()}.png")
