import utils
import classes

# literals = ["あ", "か", "き", "こ", "く"]
literals = ["ア", "カ", "キ", "コ", "ク"]
codepoints = list(map(utils.encode_codepoint, literals))
codepoints = list(map(lambda x: f"0x{x[2::]}", codepoints))

images_paths = utils.load_images_paths("kanji_mouse_drawn")
dataframe = utils.create_dataframe(images_paths, True)
images = [
    dataframe["image"][30],
    dataframe["image"][10],
    dataframe["image"][15],
    dataframe["image"][20],
    dataframe["image"][99],
]
literals = [
    dataframe["literal"][30],
    dataframe["literal"][10],
    dataframe["literal"][15],
    dataframe["literal"][20],
    dataframe["literal"][99],
]

utils.display_image(images, literals)
