#!/usr/bin/env bash

# 显示定义
STR="学而时习之"
echo $STR

# ${}
STR11="不亦说乎"
echo ${STR11}

echo "$STR11"
echo "${STR}11"

# 语句赋值
for file in `ls /etc`
do
    echo "current file: $file"
done

echo "-----"

for file in $(ls /etc)
do
    echo "current file: $file"
done

# 变量重定义
HELLO="Hello"
echo $HELLO

HELLO="Hello World"
echo $HELLO

# readonly
myUrl="https://www.xxx.com"
readonly myUrl

myUrl="http://www.xxx.com"
# myUrl: readonly variable

# unset
NUM=100
echo $NUM
unset NUM
echo $NUM
