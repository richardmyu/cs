# -*- coding: utf-8 -*-

# 3.1901 年 1 月 1 日 (周二) 至 2000 年 12 月 31 日期间共有多少周日和每月 1 号重合
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


def year_to_year(end):
    if end < 1800:
        print("输入年份有误")
        return 0

    days = 0

    for year in range(1901, end):
        if is_leap_year(year):
            days += 366
        else:
            days += 365
    return days


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


def how_week():
    sum_days = 0
    count = 0  # 重合个数
    str_date = ""  # 重合日期
    for i in range(1901, 2001):
        for j in range(1, 13):
            sum_days = year_to_year(i) + month_day(j, is_leap_year(i))
            # 1901-01-01 是周二，取余 6 才能对应周一
            if sum_days % 7 == 6:
                count += 1
                # 输出月份时要加 1
                if j + 1 < 12:
                    str_date = str_date + str(i) + "-" + str(j + 1) + ";"
                else:
                    # 若加 1 月后超出正常 12 月，则计入下一年（进一年，月份一定要重设 1）
                    str_date = str_date + str(i + 1) + "-" + str(1) + ";"

            else:
                continue
    print("counter is: %d", count)
    print("string is: %s", str_date)
    return count


print(how_week())
