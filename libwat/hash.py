import json
import re
from pathlib import Path


def check_hash(data, text):
    matches = []
    for i in data:
        if re.match(data[i], text):
            matches.append(i)

    return matches


def load_data():
    file = Path(__file__).parent / 'data' / 'hashes.json'
    with open(file) as f:
        return json.load(f)
