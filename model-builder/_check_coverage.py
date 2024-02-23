import json
import xmltodict
import utils
import random

# with open("kanjidic2/kanjidic2.xml", "r", encoding="utf-8") as xml_file:
#     data_dict = xmltodict.parse(xml_file.read())

#     # jouyou_kanji = []
#     # jouyou_kanji_literals = []
#     frequency_kanji = []
#     frequency_kanji_literals = []
#     count = 0
#     # print(data_dict["kanjidic2"]["character"][0]["misc"]["grade"])
#     for character in data_dict["kanjidic2"]["character"]:
#         try:
#             if character["misc"]["freq"]:
#                 count = count + 1
#                 frequency_kanji.append(character)
#                 frequency_kanji_literals.append(character["literal"])
#         except KeyError:
#             continue

#     print(count, "out of", 2501)

#     frequency_kanji_json = json.dumps(frequency_kanji)
#     frequency_kanji_literals_json = json.dumps(frequency_kanji_literals)

#     with open("kanjidic2/frequency_kanji.json", "w") as json_file:
#         json_file.write(frequency_kanji_json)

#     with open("kanjidic2/frequency_kanji_literals.json", "w") as json_file:
#         json_file.write(frequency_kanji_literals_json)

# etl9b = json.load(open("sets/ETL9B.json"))
# frequency = json.load(open("kanjidic2/frequency_kanji_literals.json"))
# frequency_details = json.load(open("kanjidic2/frequency_kanji_literals.json"))

# count = 0
# for literal in etl9b:
#     if utils.decode_codepoint(literal) in frequency:
#         count = count + 1
# print(count, "out of", 2501)


# --------------------------
# --------------------------
# --------------------------


# etl9b = json.load(open("sets/etl9b.json"))

# with open("kanjidic2/kanjidic2.xml", "r", encoding="utf-8") as xml_file:
#     data_dict = xmltodict.parse(xml_file.read())

#     literals_per_grade = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 8: []}
#     count = 0
#     # print(data_dict["kanjidic2"]["character"][0]["misc"]["grade"])
#     for character in data_dict["kanjidic2"]["character"]:
#         try:
#             grade = int(character["misc"]["grade"])
#             if grade <= 8 and utils.encode_codepoint(character["literal"]) in etl9b:
#                 count = count + 1
#                 literals_per_grade[grade].append(character["literal"])
#         except KeyError:
#             continue

#     sample_per_grade = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 8: []}
#     for grade, literals in literals_per_grade.items():
#         # print(grade)
#         # print(literals)
#         x = round((len(literals) / count) * 100)
#         samples = random.sample(literals, x)
#         sample_per_grade[grade] = [utils.encode_codepoint(sample) for sample in samples]

#     samples = json.dumps(sample_per_grade)

#     with open("sets/samples.json", "w") as json_file:
#         json_file.write(samples)

#     with open("kanjidic2/frequency_kanji_literals.json", "w") as json_file:
#         json_file.write(frequency_kanji_literals_json)


# --------------------------
# --------------------------
# --------------------------


# etl9b = json.load(open("sets/kuzushiji-kanji.json"))
# filltered = json.load(open("kanjidic2/jlpt_kanji_literals.json"))
# # filltered_details = json.load(open("kanjidic2/frequency_kanji_literals.json"))

# count = 0
# for literal in etl9b:
#     if utils.decode_codepoint(literal) in filltered:
#         count = count + 1
# print(count, "out of", len(filltered))


# --------------------------
# --------------------------
# --------------------------


# etl9b = json.load(open("sets/kuzushiji-kanji.json"))
filltered_1 = json.load(open("kanjidic2/jlpt_kanji_literals.json"))
filltered_2 = json.load(open("kanjidic2/jouyou_kanji_literals.json"))
filltered_3 = json.load(open("kanjidic2/frequency_kanji_literals.json"))
# # filltered_details = json.load(open("kanjidic2/frequency_kanji_literals.json"))

# count = 0
unique_kanji = set()
for arr in [filltered_1, filltered_2, filltered_3]:
    # for i in arr:
    #     unique_kanji.add(i)
    for i in arr:
        if i in filltered_1 and i in filltered_2 and i in filltered_3:
            unique_kanji.add(i)

print(len(unique_kanji))
