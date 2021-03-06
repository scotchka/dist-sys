import json
import atexit

try:
    f = open("data.json")
except FileNotFoundError:
    data = {}
    f = open("data.json", "w")
    json.dump(data, f)
else:
    data = json.load(f)
finally:
    f.close()


def save():
    with open("data.json", "w") as f:
        json.dump(data, f)


def process(text):
    command, option = text.strip().split()
    if command == "get":
        key = option
        return data[key]
    if command == "set":
        key, value = option.split("=")
        data[key] = value
        return "OK"


atexit.register(save)

while True:
    try:
        text = input("> ")
    except KeyboardInterrupt:
        break
    else:
        print(process(text))
