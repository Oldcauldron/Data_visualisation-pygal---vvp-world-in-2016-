
import json
from pygal.maps.world import COUNTRIES


def bicode(name):
    with open('add_correct_cods.json') as acc:
                correct = json.load(acc)
    for a, b in COUNTRIES.items():
        if b == name:
            return a
    if name in correct:
        return correct[name]
    return None

