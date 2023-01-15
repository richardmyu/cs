# -*- coding: utf-8 -*-

import time
import json
import pygal
import math

filename = 'btc_close_2017.json'
dates = []
months = []
weeks = []
weekdays = []
close = []

with open(filename) as f:
    btc_data = json.load(f)

    for item in btc_data:
        dates.append(item['date'])
        months.append(int(item['month']))
        weeks.append(int(item['week']))
        weekdays.append(item['weekday'])
        close.append(int(float(item['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart._title = '收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20  # step=20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('收盘价（￥）', close_log)
line_chart.render_to_file(f'收盘价对数变换折线图.svg')
