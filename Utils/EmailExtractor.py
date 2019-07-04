from extractor import Extractor
import os

def parse(sentence):
    ex = Extractor()
    email = ex.extract_email(sentence)
    return email if email is None else " ".join(email)

def elicit_flag(message):
    return message[os.path.basename(__file__).replace(".py", "")] is None, True

def elicit_sentence(message):
    return "请输入抄送邮箱"
