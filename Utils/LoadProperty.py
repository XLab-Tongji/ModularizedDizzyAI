import json
import os
import importlib
from InsertIntoDB import insertIntoDB

def load_property(name):
    with open(os.path.dirname(__file__) + '/mapping.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)
        return mapping.get(name)

# 测试主函数
if __name__ == '__main__':
    from stanfordcorenlp import StanfordCoreNLP
    with StanfordCoreNLP(r'E:/tools/stanford-corenlp-full-2018-10-05', lang='zh', memory='4g', quiet=True) as nlp:
        nlp.parse("test")

        from Staff import Staff
        staff = Staff("001", "倪奕玮", "徐锦程", "同济大学")
        config = load_property("leave")
        module = importlib.import_module(config["file"])
        while True:
            print("你要做什么呢")
            sentence = input()
            if module.entry(sentence):
                message = module.ask(sentence, config["component"], nlp)
                print(staff.toString() + module.format(message))
                print("-----------------")
                print(message)
                # 将数据插入influxdb，参见InsertIntoDB.py
                # insertIntoDB(message)


