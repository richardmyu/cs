# -*- coding: utf-8 -*-

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_1 = 'sitka_weather_2014.csv'
filename_2 = 'death_valley_2014.csv'


def get_weather(file):
    dates, highs, lows = [], [], []
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], r'%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])

            except:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return [dates, highs, lows]


def handler_plt(dates,
                highs,
                lows,
                highs_color='red',
                lows_color='blue',
                between_color='green'):
    global plt
    plt.plot(dates, highs, c=highs_color, alpha=0.5)
    plt.plot(dates, lows, c=lows_color, alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor=between_color, alpha=0.5)


def render_weather():
    global plt
    fig = plt.figure(dpi=128, figsize=(10, 6))
    [dates_1, highs_1, lows_1] = get_weather(filename_1)
    [dates_2, highs_2, lows_2] = get_weather(filename_2)

    handler_plt(dates_1, highs_1, lows_1)
    handler_plt(dates_2,
                highs_2,
                lows_2,
                highs_color='yellow',
                lows_color='orange',
                between_color='cyan')

    title = 'Daily high and low tempratures - 2014\nDeath Valley VS Sitka'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)

    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


render_weather()
