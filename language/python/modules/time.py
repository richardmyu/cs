import time

#####################
#    time.gmtime    #
#####################
# print(time.gmtime())
# time.struct_time(tm_year=2023, tm_mon=5, tm_mday=4, tm_hour=12, tm_min=45, tm_sec=22, tm_wday=3, tm_yday=124, tm_isdst=0)


# print(time.gmtime(0))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

###################
#    time.time    #
###################
"""
参数：无需参数；传入参数报错
返回自 1970-01-01 00:00:00 以来的时间，以秒表示的浮点数
"""
# print(time.time())
# 1683204518.954535

####################
#    time.ctime    #
####################
"""
参数：
    没有参数：返回当前时间
    有参数（日期-时间的毫秒表示）：返回指定时间
"""
# print(time.ctime())
# Thu May  4 20:54:20 2023

# print(time.ctime(1683204518.954535))
# Thu May  4 20:48:38 2023

####################
#    time.sleep    #
####################
"""
延迟执行
参数：延迟时间
"""
"""
for i in range(10):
    if i % 2 == 0:
        time.sleep(2)
    else:
        time.sleep(1)
    print('-' * i)
"""

########################
#    time.localtime    #
########################
# print(time.localtime())
# time.struct_time(tm_year=2023, tm_mon=5, tm_mday=5, tm_hour=21, tm_min=40, tm_sec=43, tm_wday=4, tm_yday=125, tm_isdst=0)
# print(time.localtime(1683204518.954535))
# time.struct_time(tm_year=2023, tm_mon=5, tm_mday=4, tm_hour=20, tm_min=48, tm_sec=38, tm_wday=3, tm_yday=124, tm_isdst=0)

########################
#    time.localtime    #
########################
# print(time.mktime(time.localtime()))
# 1683294178.0
# print(time.mktime(time.localtime(1683204518.954535)))
# 1683204518.0


#######################
#    time.strftime    #
#######################
print(time.strftime("%a, %d, %Y %H:%M:%S",time.gmtime()))
# Fri, 05, 2023 13:46:36

print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
# 2023-05-05 13:46:36

print(time.strftime("%a, %d, %Y %H:%M:%S",time.gmtime(1683204518.954535)))
# Thu, 04, 2023 12:48:38

print(time.strftime("%Y/%m/%d %H:%M:%S",time.gmtime(1683204518.954535)))
# 2023/05/04 12:48:38
