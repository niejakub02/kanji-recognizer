import json
import xmltodict
import utils
import random

# with open("kanjidic2/kanjidic2.xml", "r", encoding="utf-8") as xml_file:
#     data_dict = xmltodict.parse(xml_file.read())

#     # jouyou_kanji = []
#     # jouyou_kanji_literals = []
#     filltered_kanji = []
#     filltered_kanji_literals = []
#     count = 0
#     # print(data_dict["kanjidic2"]["character"][0]["misc"]["grade"])
#     for character in data_dict["kanjidic2"]["character"]:
#         try:
#             if character["misc"]["jlpt"]:
#                 count = count + 1
#                 filltered_kanji.append(character)
#                 filltered_kanji_literals.append(character["literal"])
#         except KeyError:
#             continue

#     print(count, "out of", 2230)

#     frequency_kanji_json = json.dumps(filltered_kanji)
#     frequency_kanji_literals_json = json.dumps(filltered_kanji_literals)

#     with open("kanjidic2/jlpt_kanji.json", "w") as json_file:
#         json_file.write(frequency_kanji_json)

#     with open("kanjidic2/jlpt_kanji_literals.json", "w") as json_file:
#         json_file.write(frequency_kanji_literals_json)

kuzushiji = list(
    map(lambda path: path.split("\\")[-1], utils.load_images_paths("kkanji2"))
)

with open("sets/kuzushiji-kanji.json", "w") as json_file:
    json_file.write(json.dumps(kuzushiji))
