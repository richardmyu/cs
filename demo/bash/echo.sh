#!/usr/bin/env bash

echo "It is a test"
# 或
echo It is a test

echo "\"It is a test\""
# 或
echo \"It is a test\"

# 显示变量
name=Jack
echo "$name, it is a test."

# 显示换行
echo -e "OK!\n"
echo "It is a jock"

# 显示不换行
echo -e "OK! \c"
echo "It is a jock"

# 显示结果定向至文件
# echo "It is a test" > test.log.md

# 原样输出字符串，不进行转义或取变量(用单引号)
echo -e '$name\"'

# 显示命令执行结果
echo `date`
