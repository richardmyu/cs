#!/usr/bin/env bash

# 单引号
num=112

str='this ${num} \\n'
echo $str

str1='this is '$num'!'
echo $str $str1

# 双引号
numS=113

strS="this ${numS} \\n"
echo $strS

strS1="this is "$numS"!"
echo $strS $strS1

# 不要引号
noStr=thisiszhangsan

echo $noStr

# 字符长度
echo ${#noStr}

# 提取子串

echo ${noStr:0:6}

# 查找子串
echo `expr index "$noStr" is`

# 数组定义与读取
ary=(1 2 3)
echo $ary
echo ${ary}
echo ${ary[1]}
echo ${ary[@]}
echo ${ary[*]}

ary[3]=4
echo ${ary[@]}
echo ${ary[*]}
echo ${ary[9]}

# 数组长度
echo ${#ary[@]}

echo ${#ary[*]}

# 多行注释
:<<EOF
数据的恢复时间
数据的恢复时间
数据的恢复时间
数据的恢复时间
数据的恢复时间
EOF

:<<!
扩大解放和改革
扩大解放和改革
扩大解放和改革
扩大解放和改革
!
