from extractor import Extractor
import os

def parse(sentence):
    ex = Extractor()
    name = ex.extract_name(sentence)
    return name if name is None else "".join(name)

def elicit_flag(message):
    return message[os.path.basename(__file__).replace(".py", "")] is None, True

def elicit_sentence(message):
    return "请输入您的审批人姓名"
