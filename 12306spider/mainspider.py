import requests
import json

def readfile(filename):
    trans = open(filename,"r")
    filetxt = trans.read()
    transinfo = json.loads(filetxt)
    trans.close()
    return transinfo

def landinfo(datetime,start_land,end_land):
    filename = "landinfo.txt"
    new_info = readfile(filename)
    if start_land in new_info.keys() and end_land in new_info.keys():#判断起始站,终点是否存在
        start = new_info[start_land]
        end = new_info[end_land]
        url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(datetime, start, end)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"}
        res = requests.get(url,headers=headers)
        shuju = res.text
        resinfo = json.loads(shuju)
        transinfo = resinfo["data"]["result"]
        for raw_train in transinfo:
            # 循环遍历每辆列车的信息
            data_list = raw_train.split('|')
            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_name = start_land
            # 终点站
            to_station_name = end_land
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_used_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30] or '--'
            # 软卧
            soft_sleep = data_list[23] or '--'
            # 硬卧
            hard_sleep = data_list[28] or '--'
            # 硬座
            hard_seat = data_list[29] or '--'
            # 无座
            no_seat = data_list[26] or '--'

            list = (
                '车次:{} 出发站:{} 目的地:{} 出发时间:{} 到达时间:{} 火车运行时间:{} 座位情况：\n 一等座：「{}」 二等座：「{}」 软卧：「{}」 硬卧：「{}」 硬座：「{}」 无座：「{}」'.format(
                    train_no, from_station_name, to_station_name, start_time, arrive_time, time_used_up,
                    first_class_seat, second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))

            print('*' * 100)
            print(list)
            print('*' * 100)
    else:
        print("未找到起始站点或终点站，退出")

if __name__=="__main__":
    #input输入参数
    start_land=input("起始站点:")
    end_land=input("终点站:")
    datetime=input("日期[例如：2019-07-11]:")
    landinfo(datetime,start_land,end_land)
