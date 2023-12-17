import torch
from classes import BasicNetwork
from torchvision.transforms.functional import convert_image_dtype
from torchvision.io import read_image, ImageReadMode

with torch.no_grad():
    img = convert_image_dtype(
        read_image("./test_2.png", ImageReadMode.GRAY), dtype=torch.float
    )
    # print(img.shape)
    model = BasicNetwork()
    model.load_state_dict(torch.load("./models/1_15/model_1_15.pt"))
    model.eval()
    # print(img.shape)
    pred = model(img)
    print(pred.argmax())
