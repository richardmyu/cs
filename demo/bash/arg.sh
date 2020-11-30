#!/usr/bin/env bash

echo "Shell 传递参数实例！"
echo "执行的文件名：$0"
echo "第一个参数为：$1"
echo "第二个参数为：$2"
echo "第三个参数为：$3"

echo '-------'

echo "参数个数：$#"
echo "参数：$*"
echo "参数：$@"

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done

echo '-------'

echo "当前进程ID号：$$"
echo "最后一个进程ID号：$!"

echo '-------'

echo "当前选项：$-"
echo "最后命令的退出状态：$?"

read -p "wait a minute" n
