import json
import utils

sampels_per_grade = json.load(open("sets/samples.json"))

for grade, samples in sampels_per_grade.items():
    print("GRADE: ", grade)

    for index, sample in enumerate(samples):
        print(index, ":", utils.decode_codepoint(sample))
