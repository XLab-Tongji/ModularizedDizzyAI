import re
import os

def parse(sentence):
    types = ["事", "病", "婚"]
    for t in types:
        match_obj = re.search(r'(.*)' + t + '(.*)假(.*).*', sentence, re.M | re.I)
        if match_obj:
            return t + "假"
    return None

def elicit_flag(message):
    return message[os.path.basename(__file__).replace(".py", "")] is None, True

def elicit_sentence(message):
    return "请输入请假类型"
