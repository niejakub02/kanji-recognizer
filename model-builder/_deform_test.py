import os
import utils
from torchvision.transforms.functional import convert_image_dtype
from torchvision.io import read_image, ImageReadMode
import torch
from torchvision.transforms import ToPILImage, v2

path = f"{os.getcwd()}/CUSTOM/U+4e7e/b504e193-f681-4e99-877c-bbf602786b3b.png"

img = convert_image_dtype(read_image(path, ImageReadMode.GRAY), dtype=torch.float)

transforms = v2.Compose(
    [
        v2.RandomPerspective(distortion_scale=0.1, p=1),
        v2.RandomRotation(degrees=(-2, 2)),
        v2.ElasticTransform(alpha=[200, 450], sigma=[12, 15]),
        # v2.RandomAdjustSharpness(sharpness_factor=2, p=0.5),
        v2.RandomAffine(degrees=(-2, 2), translate=(0.01, 0.06), scale=(0.98, 1.02)),
        # v2.ToPILImage(),
    ]
)
img2 = transforms(img)
img3 = transforms(img)
img4 = transforms(img)
img5 = transforms(img)
utils.display_image(
    [img, img2, img3, img4, img5],
    ["orginal", "tweaked", "tweaked", "tweaked", "tweaked"],
)
