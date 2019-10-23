import json
import os
import importlib
import urllib.request


def load_property(name):
    with open(os.path.dirname(__file__) + '/mapping.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)
        return mapping.get(name)

if __name__ == '__main__':
    config = load_property("leave")
    module = importlib.import_module(config["file"])
    from Staff import Staff
    staff = Staff("001", "倪奕玮", "徐锦程", "同济大学")
    while True:

        print("你要做什么呢")
        sentence = input()
        if module.entry(sentence):
            standord_nlp = urllib.request.urlopen('http://127.0.0.1:8081/server')
            message = module.ask(sentence, config["component"], standord_nlp)
            print(staff.toString() + module.format(message))
            print("-----------------")
            print(message)