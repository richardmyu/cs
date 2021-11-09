# -*- coding: utf-8 -*-

# 已知 1800 年 1 月 1 日是周三，则对于一个给定的年份和月，输出这个月最后一天是周几

# 闰年 还是 平年
def is_leap_year(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    elif y % 4 == 0:
        return True
    else:
        return False


# print(is_leap_year(2000))
# print(is_leap_year(1800))
# print(is_leap_year(1900))
# print(is_leap_year(1804))

# m 月最后一天距当年 1 月 1 号的天数
def month_day(m, y=False):
    if y:
        if m == 1:
            return 31
        elif m == 2:
            return 60
        elif m == 3:
            return 91
        elif m == 4:
            return 121
        elif m == 5:
            return 152
        elif m == 6:
            return 182
        elif m == 7:
            return 213
        elif m == 8:
            return 244
        elif m == 9:
            return 274
        elif m == 10:
            return 305
        elif m == 11:
            return 335
        elif m == 12:
            return 366
        else:
            print("月份错误")
            return
    else:
        if m == 1:
            return 31
        elif m == 2:
            return 59
        elif m == 3:
            return 90
        elif m == 4:
            return 120
        elif m == 5:
            return 151
        elif m == 6:
            return 181
        elif m == 7:
            return 212
        elif m == 8:
            return 243
        elif m == 9:
            return 273
        elif m == 10:
            return 304
        elif m == 11:
            return 334
        elif m == 12:
            return 365
        else:
            print("月份错误")
            return


# print(month_day(1))
# print(month_day(2))
# print(month_day(2, True))
# print(month_day(11))
# print(month_day(12))

# 起始年到终止年的天数
def year_to_year(end):
    if end < 1800:
        print("输入年份有误")
        return 0

    days = 0

    for year in range(1800, end):
        if is_leap_year(year):
            days += 366
        else:
            days += 365
    return days


# print(year_to_year(1804))

# 周几
def get_week(d):
    if d == 0:
        # return "周三"
        return 3
    elif d == 1:
        # return "周四"
        return 4
    elif d == 2:
        # return "周五"
        return 5
    elif d == 3:
        # return "周六"
        return 6
    elif d == 4:
        # return "周日"
        return 7
    elif d == 5:
        # return "周一"
        return 1
    else:
        # return "周二"
        return 2


def how_week(y, m):
    sum_days = 0
    sum_days = year_to_year(y) + month_day(m, is_leap_year(y)) - 1
    mod_day = sum_days % 7
    return get_week(mod_day)


print(how_week(2033, 12))  # 6
print(how_week(2020, 12))  # 4
print(how_week(2000, 7))  # 1
