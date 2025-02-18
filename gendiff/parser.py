import json


def parse(file_path):
    return json.load(open(file_path))
