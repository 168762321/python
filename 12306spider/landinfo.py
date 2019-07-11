# -*- coding: UTF-8 -*-
#处理火车站信息，下载下来保存,生成一个landinfo.txt文件
import requests
import json
land={}
def down_landinfo(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"}
    res = requests.get(url,headers=headers)
    info = res.text
    reinfo = info.split("@")
    del reinfo[0]
    for i in reinfo:
        key = i.split("|")[1]
        value = i.split("|")[2]
        land[key]=value
    landinfo = json.dumps(land)
    with open("landinfo.txt", "w") as code:
        code.writelines(landinfo)
        code.close()
        print("文件生成结束")
if __name__=="__main__":
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9106"
    down_landinfo(url=url)