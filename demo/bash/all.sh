#!/bin/bash
# learn bash

# echho 后面单引号和双引号的作用不一样的
# 双引号可以进行运算、转换
# 单引号则不会，默认全字符串输出
echo "Hello World!"

# 显示当前 shell
# echo $SHELL

# 参数

# $0 命令本身
# echo $0
# echo $1 $2 $3
# 全部参数（整体）
# echo $*

# 全部参数（独立体）
# echo $@

# 参数个数
# echo $#

# echo 当前进程的PID进程号=$$

# &: 以后台的方式运行程序
# ./hello.sh &

# echo 最后一个进程的PID进程号=$!

# echo 最后执行的命令结果=$?


# 显示当前环境变量
# env

# 显示用户
# whoami



# 运算
# $(())
# echo $(((2+3)*4))

# $[]
# echo $[(2 + 3) * 4]

# TEMP=`expr 2 + 3`
# echo `expr $TEMP \* 4`

# 条件判断 [ condition ]
# condition 前后必须要有空格

# if [ 'test' = 'test' ]
# then
#     echo '等于'
# fi

# # 20 > 10 ?
# if [ 20 -gt 10 ]
# then
#     echo '大于'
# fi

# 是否存在文件

# if [ -e /root/shell/a.txt ]
# then
#     echo '存在'
# fi

# if [ 'test00' = 'test00' ] && echo 'hello' || echo 'world'
# then
#     echo '条件满足，执行后续语句'
# fi

# 流程控制

# if [ $1 -ge 60 ]
# then
#     echo '及格'
# elif [ $1 -lt 60 ]
# then
#     echo '不及格'
# fi

# case

# case $2 in
# "1")
# echo '周一'
# ;;
# "2")
# echo '周二'
# ;;
# *)
# echo '其他'
# ;;
# esac

# for 循环

# for i in "$*"
# do
#     echo "the arg is $i"
# done

# echo '-----'

# for j in "$@"
# do
#     echo "the arg is $j"
# done

# echo '-----'

# for z in "$*" "$@"
# do
#     echo "is $z"
# done

# SUM=0
# for ((i=1;i<=100;i++))
# do
#     echo "num is $i"
#     SUM=$[$SUM + $i]
# done

# echo $SUM

# SUM=0
# for i in 100
# do
#     echo '$i'
#     SUM=$(($SUM + $i))
# done

# echo $SUM

# while 循环

# SUM=0
# i=0

# while [ $i -le $1 ]
# do
#     SUM=$(($SUM+$i))
#     i=$(($i+1))
# done

# echo $SUM

# 读取控制台输入

read -p "请输入一个数num1=" NUM1
echo "你输入的数num1的值是：$NUM1"

# 不支持 -t
read -t 10 -p "请在10 秒内输入一个数num2=" NUM2
echo "你输入的数num2的值是：$NUM2"

# 系统函数

# basename 删除路径最后一个 / 前的所有部分（包括 /），常用于获取文件名
# basename [pathname] [suffix]
# basename [string] [suffix]
# basename /usr/bin/sort

# basename /usr/bin/sort.h

# 若指定 suffix，则会删除后缀
# basename /usr/bin/sort.h .h

# dirname 删除路径最后一个 / 后所有部分（包括 /），常用于获取文件路径
# dirname pathname
# 若不含 /，则返回 '.'(当前路径)
# dirname /usr/bin/sort

# dirname /usr/bin/sort /bin/sort1

# dirname helloworld

# 自定义函数
# function getSum() {
#   echo "---"
#   SUM=$(($n+$m))
#   echo "sum=$SUM"
# }

# read -p "请输入第一个数n：" n
# read -p "请输入第二个数m：" m

# # 调用函数
# getSum $n $m

read -t 5 -p "请输入随机数s: " s
