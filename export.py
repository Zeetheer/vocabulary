import json
import re


def export(place):
    if place == "":
        pass
    else:
        file = open(place, "w")
        with open("vocabulary.json", "r", encoding="UTF8") as vocajson:
            voca = json.load(vocajson)
            data = f"{voca}".replace("{", "")
            data = data.replace("}", "")
            data = data.replace("'jvocabulary': ", "")
            data = data.replace("'", "")
            data = data.replace(",", "\n")
            data = " " + data
            file.write(data)
