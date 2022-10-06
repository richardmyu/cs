# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from urllib.request import urlopen
import json
# import requests
import pygal

# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# github 上的 json 请求不到

# response = urlopen(json_url)

# # 读取数据
# req = response.read()

# # 将数据写入文件
# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)

# # 加载 json 格式
# file_urllib = json.loads(req.decode('utf8'))
# print(file_urllib)

# req = requests.get(json_url)
# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)
# file_requests = req.json()
# print(file_requests)

filename = 'btc_close_2017.json'
dates = []
months = []
weeks = []
weekdays = []
close = []

with open(filename) as f:
    btc_data = json.load(f)

    # for item in btc_data:
    #     date = item['date']
    #     month = int(item['month'])
    #     week = int(item['week'])
    #     weekday = item['weekday']
    #     close = int(float(item['close']))
    #     print(
    #         f'{date} is month {month} week {week}, {weekday}, the close price is {close} RMB.'
    #     )
    for item in btc_data:
        dates.append(item['date'])
        months.append(int(item['month']))
        weeks.append(int(item['week']))
        weekdays.append(item['weekday'])
        close.append(int(float(item['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart._title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价（￥）', close)
line_chart.render_to_file('收盘价折线图.svg')
