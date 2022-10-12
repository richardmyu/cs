#!/usr/bin/env bash

# 数值测试
num1=100
num2=100
if test $[num1] -eq $[num2]
then
    echo '两个数相等！'
else
    echo '两个数不相等！'
fi

result=$[num1+num2]
echo "result 为：$result"

# 字符串测试
str1="ru1noob"
str2="runoob"
if test $str1 = $str2
then
    echo '两个字符串相等!'
else
    echo '两个字符串不相等!'
fi

# 文件测试
cd /bin
if test -e ./bash
then
    echo '文件已存在!'
else
    echo '文件不存在!'
fi

cd /bin
if test -e ./notFile -o -e ./bash
then
    echo '至少有一个文件存在!'
else
    echo '两个文件都不存在'
fi
