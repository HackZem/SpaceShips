import json


def openTxt(file):
    with open(file, "r") as txt:
        info = json.load(txt)
        txt.close()

    return info


def writeTxt(file, input_txt):
    with open(file, "w") as txt:
        json.dump(input_txt, txt)
        txt.close()
