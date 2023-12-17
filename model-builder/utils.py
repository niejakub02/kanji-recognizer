import os
from glob import glob
import torch
from torchvision.transforms import ToPILImage
from torchvision.transforms.functional import convert_image_dtype
from torchvision.io import read_image, ImageReadMode
from pandas import DataFrame
import matplotlib.pyplot as plt
import torch.nn as nn
import json
from consts import matplotlib_title_font, CLASSES_COUNT, text_emphasis as te
import argparse


def display_image(
    tensor: torch.Tensor | list[torch.Tensor], literal: str | list[str] = "unknown"
):
    """
    Takes a tensor or list of tensors and displays them in a plot.\n
    Images are displayed in grayscale.
    """
    if (
        isinstance(tensor, list)
        and isinstance(literal, list)
        and len(tensor) == len(literal)
    ):
        fig, axs = plt.subplots(1, len(tensor))
        for i, (_tensor, _literal) in enumerate(zip(tensor, literal)):
            axs[i].set_title(_literal, matplotlib_title_font)
            axs[i].set_axis_off()
            axs[i].imshow(ToPILImage()(_tensor), cmap="gray")

    elif isinstance(tensor, torch.Tensor) and isinstance(literal, str):
        plt.title(literal, matplotlib_title_font)
        plt.imshow(ToPILImage()(tensor), cmap="gray")
        plt.axis("off")

    else:
        raise Exception("Invalid data format")

    plt.tight_layout()
    plt.rcParams["axes.unicode_minus"] = False
    plt.show()


def load_images_paths(path: str, set: list[str] | None = None):
    """
    Fetches paths to images from folder.\n
    Structure of ./<path>/<class_identifier>/((images)) is expected.\n

    Legend:\n
    <path> - argument passed to function, can be either string of folder name,
    but also path like "../../public/images".\n
    <class_identifier> - name that will be used as class identifier (literal).\n
    ((images)) - images files
    """
    if set is None:
        return glob(rf"{os.getcwd()}\{path}\*")
    else:
        arr = []
        for i in set:
            arr.append(glob(rf"{os.getcwd()}\{path}\{i}")[0])
        return arr


def load_set(path: str):
    with open(f"{os.getcwd()}/{path}") as json_file:
        return json.load(json_file)


def create_dataframe(images_paths: list[str], convert_to_tensor: bool = False):
    dictionary = []
    # # test
    # count = 0
    # for i in images_paths:
    for i in images_paths:
        arr = glob(rf"{i}\*.png")
        unicode = i.split("\\")[-1]
        literal = decodeCodepoint(unicode)

        # # test
        # if len(arr) < 100 or len(arr) > 100:
        #     continue
        # print(literal, i, len(arr))
        print(literal, i, len(arr))

        for image_path in arr:
            dictionary.append(
                {
                    "image": convert_image_dtype(
                        read_image(image_path, ImageReadMode.GRAY), dtype=torch.float
                    )
                    if convert_to_tensor
                    else image_path,
                    "literal": literal,
                }
            )
        #     # test
        # count += 1

        # # test
        # if count == CLASSES_COUNT:
        #     break

    return DataFrame(dictionary, columns=["image", "literal"])


def create_folder(path: str):
    if not (os.path.exists(f"{os.getcwd()}/{path}")):
        os.mkdir(f"{os.getcwd()}/{path}")


def save_best_model(validation_rate: list[float], model: nn.Module, path: str):
    if validation_rate[-1] > (
        max(validation_rate[:-1]) if len(validation_rate) > 1 else 0
    ):
        torch.save(
            model.state_dict(),
            f"{path}.pt",
        )
        print(f"{te.BOLD + te.GREEN}-- UPDATE --{te.RESET}")
    else:
        print(f"{te.BOLD + te.RED}-- FAIL --{te.RESET}")


def handle_args(MODEL_FOLDER_PATH: str):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-n",
        "--notes",
        help="provide value to save notes in model's directory, remeber to wrap message in double quotes",
    )
    args = parser.parse_args()
    config = vars(args)
    if config["notes"] is not None:
        with open(f"{MODEL_FOLDER_PATH}/notes.txt", "w") as out:
            out.write(config["notes"])


def encodeCodepoint(character: str):
    """
    Returns unicode code point
    """
    return f"U+{character.encode('unicode_escape').decode('utf8')[2::]}"


def decodeCodepoint(character: str):
    """
    Returns literal (utf-16)
    """
    return chr(int(character[2::], 16))
