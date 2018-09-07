# cp936
import requests
import sys
import re


while True:
    c_name = input('请输入需要查询的城市名称：')
    url = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%c_name

    try:
        req = requests.get(url)
        data = req.json()
        data['data']
    except:
        print('抱歉，未能获取此城市的天气情况...')
        sys.exit()

    w_yesterday = data['data']['yesterday']

    print ('昨天回顾\n '+ w_yesterday['date']+'\t'+ w_yesterday['type'])
    print (w_yesterday['high'] +'\t'+ w_yesterday['low'])
    print('风向 '+ w_yesterday['fx']+'\t'+'风速 '+ re.search('[0-9]级',w_yesterday['fl']).group()+'/n')

    print ('未来天气')
    for w in data['data']['forecast']:
        print(w['date']+'\n' +w['type'])
        print(w['high'] + '\t' + w['low'])
        print('风向 ' + w['fengxiang'] + '\t' + '风速 ' + re.search('[0-9]级', w['fengli']).group()+'/n')

    print('当前温度：'+data['data']['wendu'])
    print('贴士：'+data['data']['ganmao'])

    choose = input('是否需要继续查询，继续请按 y ，退出请按其余任意键\n')
    if choose == 'y':
        continue
    else:
        sys.exit()


