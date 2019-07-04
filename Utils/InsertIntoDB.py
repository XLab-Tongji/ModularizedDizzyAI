import datetime
from influxdb import InfluxDBClient
def insertIntoDB(message):
    client = InfluxDBClient(host='10.60.38.173', port=8086, username='root', password='tongji409', database='dizzyAI')
    print(client.get_list_database())   #显示所有数据库名称
    result = client.query("show measurements")    #显示数据库中的表
    print(result)


    json_body = [
        {
            "measurement": "leave_list",
            "tags": {
                "staff": "001"
            },
            # "time": datetime.datetime.now(),
            "fields": message
            # "fields": {
            #     "value": 0.64
            # }
        }
    ]
    print(json_body)

    client.write_points(json_body)


    result2 = client.query("select * from leave_list")
    print("Result: {0}".format(result2))

    client.close()
