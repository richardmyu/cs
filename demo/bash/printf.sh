#!/usr/bin/env bash

echo "hello,world"
printf "hello,world\n"

printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" 张三 男 66.1234
printf "%-10s %-8s %-4.2f\n" 王五 男 48.6543
printf "%-10s %-8s %-4.2f\n" 李思 女 47.9876

# format-string 为双引号
printf "%d %s\n" 1 "abc"
# 1 abc

echo '------'

# 单引号与双引号效果一样
printf '%d %s\n' 1 "abc"
# 1 abc

echo '------'

# 没有引号也可以输出
printf %s abcdef
# abcdef
echo '------'


# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
printf %s abc def
# abcdef
echo '------'


printf "%s\n" abc def
# abc
# def
echo '------'

printf "%s %s %s\n" a b c_class d e f g h i j
# a b c_class
# d e f
# g h i
# j
echo '------'


# 如果没有 arguments，那么
# %s 用 NULL 代替
# %d 用 0 代替
# %c_class 用 NULL 代替
# %f 用 0.000000 代替
printf "%s and %d and %c and %f \n"
# and 0 and  and 0.000000

printf "a string, no processing:<%s>\n" "A\nB"
# a string, no processing:<A\nB>

printf "a string, no processing:<%b>\n" "A\nB"
# a string, no processing:<A
# B>

printf "www.runoob.com \a"
# www.runoob.com $                  #不换行
