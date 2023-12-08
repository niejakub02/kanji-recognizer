from glob import glob
from PIL import Image
from uuid import uuid4
from utils import create_folder
import os

PATH_ETL9B = "ETL9B"
OUTPUT_PATH = "ETL9B_CONVERTED"
LITERAL_WIDTH = 64
LITERAL_HEIGHT = 63


def get_n_columns(width) -> int:
    return int(width / LITERAL_WIDTH)


def get_n_rows(height) -> int:
    return int(height / LITERAL_HEIGHT)


if __name__ == "__main__":
    create_folder(OUTPUT_PATH)
    imgs_paths = glob(rf"{os.getcwd()}\{PATH_ETL9B}\*.png")
    txts_paths = glob(rf"{os.getcwd()}\{PATH_ETL9B}\*.txt")

    for img_path, txt_path in zip(imgs_paths, txts_paths):
        with open(txt_path, "r", encoding="utf-8") as txt:
            # removing whitespace and new lines characters
            it = iter(txt.read().strip().replace("\n", ""))
            im = Image.open(img_path)
            eof = False

            for y_start in range(
                0, get_n_rows(im.height) * LITERAL_HEIGHT, LITERAL_HEIGHT
            ):
                for x_start in range(
                    0, get_n_columns(im.width) * LITERAL_WIDTH, LITERAL_WIDTH
                ):
                    try:
                        literal = next(it)
                        code_point = literal.encode("unicode_escape").decode("utf8")
                        cropped_im = im.crop(
                            (
                                x_start,
                                y_start,
                                x_start + LITERAL_WIDTH,
                                y_start + LITERAL_HEIGHT,
                            )
                        ).resize((64, 64))
                        create_folder(f"{OUTPUT_PATH}/{code_point}")
                        cropped_im.save(
                            f"{os.getcwd()}/{OUTPUT_PATH}/{code_point}/{uuid4()}.png"
                        )
                    except StopIteration:
                        eof = True
                        break
                if eof:
                    break
