# TODO решите задачу
import json

filename = 'input.json'

def task(filename) -> float:
    s = 0
    with open(filename) as file:
        file_new = json.load(file)
        for i in file_new:
            s += i.get('score') * i.get('weight')
    return round(s, 3)

print(task(filename))
