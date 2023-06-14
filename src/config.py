# Relative path
import os

# Parse JSON
import json


directory = os.path.dirname(os.path.abspath(__file__))


def getJSON():
    try:
        with open(os.path.join(directory, '../request.json'), "r", encoding="utf8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[ERROR] request.json file NOT found")
