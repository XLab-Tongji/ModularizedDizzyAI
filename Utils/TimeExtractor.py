from TimeNLP import TimeNormalizer
from extractor import Extractor
import re
import os
import arrow

# nm = NameMatcher()
tn = TimeNormalizer()
ex = Extractor()

# 一天工作时间为8小时
WORK_HOURS = 8

# 上下班时间
GO_WORK_TIME = "09:00:00"
OFF_WORK_TIME = "17:00:00"

def parse(sentence, s_time=None, e_time=None, duration=None):
    pos, res_union = tn.parse(target=sentence)
    if len(res_union):
        for res in res_union:
            try:
                # print(res)
                if res['type'] == "timedelta":
                    duration = res['timedelta']
                    # print(duration)

                elif res['type'] == "timespan":
                    s_time = res['timespan'][0]
                    e_time = res['timespan'][1]
                elif res['type'] == "timestamp":
                    s_time = res['timestamp']
                    s_hour = str(s_time).split(' ')[1].split(':')[0]
                    # print(s_hour)
                    if s_hour == "00":
                        s_time = str(s_time).split(' ')[0] + ' ' + GO_WORK_TIME
                        # print(s_time)
                    # print(s_time)
            except:
                duration = duration
                s_time = s_time
                e_time = e_time

    a_half_day = re.search(r'(.*)(半)(.*)([天]|[日](.*))', sentence, re.M | re.I)
    more_half_day = re.search(r'((.*)([天]|[日])半(.*))|((.*)(再|还|另外|另)(.*)(加?)半(.*)([天]|[日])(.*))', sentence,
                              re.M | re.I)
    # 类似"一天半"
    if more_half_day:
        # print("more")
        duration = duration.split(', ')[0] + ', ' + str(int(WORK_HOURS / 2)) + ":00:00"
    # "半天"
    elif a_half_day:
        duration = "0 days, " + str(int(WORK_HOURS / 2)) + ":00:00"

    if s_time is not None and duration is not None:
        t_days = int(duration.split()[0])
        # t_days -= 1
        t_hours = duration.split(', ')[1]
        t_hours = int(t_hours.split(':')[0])

        # 未填入结束时间
        if e_time is None:
            e_time = s_time
            e_time = arrow.get(e_time).shift(days=+t_days).format('YYYY-MM-DD HH:mm:ss')
            e_time = arrow.get(e_time).shift(hours=+t_hours).format('YYYY-MM-DD HH:mm:ss')

        # 结束时间矛盾
        elif e_time != arrow.get(s_time).shift(days=+t_days).format('YYYY-MM-DD HH:mm:ss'):
            s_time = None
            e_time = None
            duration = None
            print("输入的请假时间矛盾，已清空")
    return s_time, e_time, duration

def elicit_flag(message):
    flag = (message["startDate"] is None and message["endDate"] is None and message["duration"] is None) or \
           (message["startDate"] is not None and message["endDate"] is None and message["duration"] is None) or \
           (message["startDate"] is None and message["endDate"] is None)
    return flag, True

def elicit_sentence(message):
    if message["startDate"] is None and message["endDate"] is None and message["duration"] is None:
        return "请输入请假时间"
    elif message["startDate"] is not None and message["endDate"] is None and message["duration"] is None:
        return "你想请几天假"
    elif message["startDate"] is None and message["endDate"] is None:
        return "请输入请假的开始时间"
