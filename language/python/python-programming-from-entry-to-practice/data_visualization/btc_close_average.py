import json
import pygal
from itertools import groupby

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


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    # groupby 分组函数，它可以实现数据的分组及组内运算
    # zip 函数用于将可迭代的对象作为参数，
    # 将对象中对应的元素打包成一个个元组，
    # 然后返回由这些元组组成的列表。
    # lambda [parameters]: expression
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])

    # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
    # [*zip(*xy_map)] == list[zip(*xy_map)]
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')

    return line_chart


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值', '月日均值')

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价周日均值', '周日均值')

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值.svg')
line_chart_weekday
