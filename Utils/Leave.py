import re
import importlib
import json
import os
import datetime
import time

def entry(sentence):
    return re.search(r'(.*)请(.*)假(.*).*', sentence, re.M | re.I)

def init(components):
    values = dict()
    for component in components:
        if component == "TimeExtractor":
            values["startDate"] = None
            values["endDate"] = None
            values["duration"] = None
        else:
            values[str(component)] = None
    return values

def ask(sentence, components, nlp=None):
    values = init(components)

    while True:
        for component in components:
            if component == "TimeExtractor":
                if values["startDate"] is None or values["endDate"] is None:
                    module = importlib.import_module(component)
                    values["startDate"], values["endDate"], values["duration"] = \
                        module.parse(sentence, values["startDate"], values["endDate"], values["duration"])
            elif component == "ReasonExtractor":
                if values[str(component)] is None:
                    module = importlib.import_module(component)
                    values[str(component)] = module.parse(sentence, nlp)
            else:
                if values[str(component)] is None:
                    module = importlib.import_module(component)
                    values[str(component)] = module.parse(sentence)
        question = continue_ask(values, components)
        if question is not None:
            print(question)
            sentence = input()
            continue

        print("确认吗？")
        sentence = input()
        deny = re.search(r'不|重(新?)(.*)(填(写?)|输(入?))|重来|打?填?写?错了?|改', sentence)
        if deny:
            values = init(components)
            print("请假信息已清空，请重新输入请假内容")
            sentence = input()
        elif "确认" in sentence:
            break
    return values

def continue_ask(message, components):
    for component in components:
        module = importlib.import_module(component)
        flag, need_return = module.elicit_flag(message)
        if flag:
            if need_return:
                return module.elicit_sentence(message)
            else:
                message = module.elicit(message)
    return None

def format(message):
    ret = ""
    with open(os.path.dirname(__file__) + '/dependency/Leave.json', 'r', encoding='utf-8') as f:
        formats = json.load(f)
        for field in formats:
            field_name = field["field"]
            if field_name in message:
                ret = ret + "【" + field["name"] + "】 "
                if field["type"] == "date":
                    date = datetime.datetime.strptime(message[field_name], "%Y-%m-%d %H:%M:%S")
                    ret = ret + date.strftime("%y/%m/%d %H:%M") + " "
                else:
                    ret = ret + message[field_name] + " "

    return ret
