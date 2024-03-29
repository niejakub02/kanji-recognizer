import os
import glob
import numpy as np
import sys
import torch
from PIL.Image import open as open_image
from torch import Tensor, nn
from torchvision import transforms
from torchvision.io import read_image, ImageReadMode
from torch.utils.data import DataLoader, random_split
from torch.optim import Adam
import matplotlib.pyplot as plt
import classes
from torchinfo import summary
from tqdm import tqdm
from consts import (
    LEARNING_RATE,
    EPOCHS_COUNT,
    BATCH_SIZE,
    MODELS_FOLDER_PATH,
    DATASET_SPLIT_RATIO,
    text_emphasis as te,
)
import torch.onnx
import json
import csv
import io
import argparse
import utils

# custom imports

# config
np.set_printoptions(threshold=sys.maxsize)
torch.set_printoptions(threshold=sys.maxsize)
IMAGES_FOLDER_NAME = "kkanji2"


if __name__ == "__main__":
    versioning_file = json.load(open("version.json", "r"))
    version = {"major": versioning_file["major"], "minor": versioning_file["minor"] + 1}
    MODEL_FOLDER_PATH = f"{MODELS_FOLDER_PATH}/{version['major']}_{version['minor']}"
    MODEL_PATH = f"{MODEL_FOLDER_PATH}/model_{version['major']}_{version['minor']}"

    # subset = load_set("sets/hiragana.json")
    # images_paths = load_images_paths(IMAGES_FOLDER_NAME, subset)
    # utils.format_drawings("katakana-mouse", IMAGES_FOLDER_NAME)
    images_paths = utils.load_images_paths(IMAGES_FOLDER_NAME)
    dataframe = utils.create_dataframe(images_paths, True)
    dataset = classes.CustomDataset(dataframe)
    # dataset = torch.load("./dataset-hiragana.pt")
    torch.save(dataset, "dataset-kuzushiji.pt")
    # dataset.adjust(["か", "も", "い", "ぽ", "く"])
    exit()
    # # load dataset
    # dataset = torch.load("./dataset.pt")

    # # how to read dataset
    # print(dataset[3][0].shape)
    # # print(dataset[3][1])

    # # sample
    # sample = dataframe.sample(10)
    # img = sample["image"].to_list()
    # lab = sample["literal"].to_list()
    # display_image(img, lab)

    utils.create_folder(MODELS_FOLDER_PATH)
    utils.create_folder(MODEL_FOLDER_PATH)

    model = classes.CNN_8()
    if torch.cuda.is_available():
        model.cuda()
    opt = Adam(model.parameters(), lr=LEARNING_RATE)
    lossFn = nn.CrossEntropyLoss()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # data_loader = DataLoader(dataset, 32, True)
    train_set, validation_set, test_set = random_split(dataset, DATASET_SPLIT_RATIO)
    train_loader = DataLoader(train_set, BATCH_SIZE, True)
    validation_loader = DataLoader(validation_set, BATCH_SIZE, True)
    test_loader = DataLoader(test_set, BATCH_SIZE, True)
    validation_rate = []
    stats = []

    # TODO: to utils
    summary_output = summary(model, (1, 1, 64, 64), verbose=0)
    with open(
        f"{MODEL_PATH}.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(str(summary_output))

    # TODO: to utils
    json_object = json.dumps(
        dict(zip(range(len(dataset.unique_labels)), dataset.unique_labels))
    )
    with open(f"{MODEL_PATH}.json", "w") as out:
        out.write(json_object)
    # print(dataset[0][0])
    # display_image(dataset[0][0])

    # loop over our epochs
    for e in range(0, EPOCHS_COUNT):
        # set the model in training mode
        model.train()

        # initialize the total training and validation loss
        total_train_loss = 0
        total_val_loss = 0

        # initialize the number of correct predictions in the training
        # and validation step
        train_correct = 0
        val_correct = 0

        # loop over the training set
        for x, y in tqdm(train_loader, desc=f"Epoch {e+1}"):
            # send the input to the device
            (x, y) = x.to(device), y.to(device)

            # perform a forward pass and calculate the training loss
            # display_image(list(x), list(y))
            pred = model(x)
            print(pred.size())
            loss = lossFn(pred, y)
            # print(x[0])
            # print(type(x[0]))
            # zero out the gradients, perform the backpropagation step,
            # and update the weights
            opt.zero_grad()
            loss.backward()
            opt.step()

            # add the loss to the total training loss so far and
            # calculate the number of correct predictions
            total_train_loss += loss.item()

            train_correct += (pred.argmax(1) == y).type(torch.float).sum().item()

        with torch.no_grad():
            # set the model in evaluation mode
            model.eval()
            # loop over the validation set
            for x, y in validation_loader:
                # send the input to the device
                (x, y) = x.to(device), y.to(device)

                # make the predictions and calculate the validation loss
                pred = model(x)
                # # to compare outputs
                # print(pred.argmax(1))
                # print(y)

                total_val_loss += lossFn(pred, y).item()
                # calculate the number of correct predictions
                val_correct += (pred.argmax(1) == y).type(torch.float).sum().item()

            train_acc = train_correct / len(train_set)
            val_acc = val_correct / len(validation_set)
            stats.append([e, total_train_loss, train_acc, total_val_loss, val_acc])
            validation_rate.append(val_acc)

            print(f"train loss: {total_train_loss}")
            print(f"training accuracy: {train_acc}")
            print(f"validation loss: {total_val_loss}")
            print(f"validation accuracy: {validation_rate[-1]}")

            utils.save_best_model(validation_rate, model, MODEL_PATH)

    # TODO to utils
    if "-n" in sys.argv:
        with open(f"{MODEL_FOLDER_PATH}/notes.txt", "w") as out:
            try:
                value = sys.argv[sys.argv.index("-n") + 1]
                out.write(value)
            except IndexError:
                print("Provided value for notes is incorrect")

    # TODO to utils
    with open(f"{MODEL_PATH}.csv", "w", newline="") as out:
        stats_headers = ["epoch", "loss", "accuracy"]
        out.write("sep=;\n")
        writer = csv.writer(out, delimiter=";")
        writer.writerow(stats_headers)
        writer.writerows(stats)

    plt.plot(validation_rate)

    testCorrect = 0
    with torch.no_grad():
        best_model = classes.CNN_8()
        best_model.load_state_dict(torch.load(f"{MODEL_PATH}.pt"))
        best_model.eval()
        for x, y in test_loader:
            (x, y) = x.to(device), y.to(device)
            pred = best_model(x)
            testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_acc = testCorrect / len(test_set)
    print(f"test accuracy: {testCorrect / len(test_set)}")
    stats.append(["TEST", "", test_acc])

    # TODO: to utils
    json_object = json.dumps(version)
    with open("version.json", "w") as out:
        out.write(json_object)

    utils.handle_args(MODEL_FOLDER_PATH)
    # switch off autograd for evaluation

    # display_image(dataset[0:8][0], dataset[0:8][1])

    # display_image(dataset[3][0])
    # print(dataframe.head(5))
    # print(dataframe["literal"].iloc[5])

    # # PIL way
    # open_image(dataframe["image"].iloc[2]).show()

    # # works for tensors
    # display_image(
    #     dataframe["image"].iloc[2:5].to_list(), dataframe["literal"].iloc[2:5].to_list()
    # )
