from utils import load_set, load_images_paths, create_dataframe
from classes import CustomDataset
import torch

IMAGES_FOLDER_NAME = "ETL6"

subset = load_set("sets/katakana.json")
images_paths = load_images_paths(IMAGES_FOLDER_NAME, subset)
# images_paths = load_images_paths(IMAGES_FOLDER_NAME)
dataframe = create_dataframe(images_paths, True)
dataset = CustomDataset(dataframe)
# dataset = torch.load("./dataset.pt")
torch.save(dataset, "./dataset-katakana.pt")
