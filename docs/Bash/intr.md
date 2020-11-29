# bash

### 1.运行

运行 Shell 脚本有两种方法：

**1.作为可执行程序**

```shell
chmod +x ./hello.sh #使脚本具有执行的权限
./hello.sh #执行脚本
```

> 注意：是 `./hello.sh` 而不是 `hello.sh`。后者，Linux 系统会去 `PATH` 中寻找 `hello.sh`，而 `PATH` 中只有 `/bin`、`/sbin`、`/usr/bin` 等等，而当前目录通常不在 `PATH` 中，所以会找不到命令无法执行。`./hello.sh` 则是指明在当前目录查找。

**2.作为解释器参数**

直接运行解释器，其参数就是 Shell 脚本的文件名：

```shell
/bin/bash hello.sh
/bin/zsh hello.sh

# 更简洁
sh hello.sh
```

> 这种方式运行脚本，不需要在第一行指定解释器（写了也没用）。

脚本也可以在 windows 的 power shell 中运行，但是需要先安装 Git，本质是调用 Git 来执行脚本。当然执行完后会自动关闭 Git 。

```shell
# windows powershell
./hello.sh
```

### 2.变量

定义变量时，变量名不加美元符号（`$`），如：

```shell
str="学而时习之"
```

> 注意：等号前后都不能由空格。

变量命名遵循以下规则：

- 命名只能使用英文字母，数字和下划线（但不能首字符不能是数字）；
- 不能使用 bash 的关键字（可以使用 help 查看保留关键字）；

出了显示地直接赋值，还可以用语句给变量赋值：

```shell
for file in `ls /etc`
# 或
for file in $(ls /etc)
```

##### 2.1.使用变量

使用已定义的变量，只需在变量前加 `$`：

```shell
echo $str
# 或
echo ${str}
```

> `${str}` 中的花括号是可选的，目的是为了帮组解释器识别变量的边界，推荐加上花括号。

```shell
echo "$STR11"
# 不亦说乎
echo "${STR}11"
# 学而时习之11
```

一定义过的变量，可以重新被定义：

```shell
HELLO="Hello"
echo $HELLO

HELLO="Hello World"
echo $HELLO
```

> 记住变量只有被使用的时候才需要加 `$` 符号。

##### 2.2.只读变量

使用 `readyonly` 命令可以将变量定义为只读变量，只读变量的值不能被改变。

```shell
myUrl="https://www.xxx.com"
readonly myUrl

myUrl="http://www.xxx.com"
# myUrl: readonly variable
```

##### 2.3.删除变量

使用 `unset` 命令可以删除变量：

```shell
NUM=100
echo $NUM
# 100

unset NUM
echo $NUM
# ''
```

##### 2.4.变量类型

运行 Shell 时，会同时存在三种变量：

1. **局部变量**：局部变量在脚本或者命令中定义，仅在当前 shell 实例中有效，其他 shell 启动的程序不能访问局部变量；
2. **环境变量**：所有的程序，包括 shell 启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要时 shell 脚本也可以定义环境变量；
3. **shell 变量**：shell 变量是由 shell 程序设置的特殊变量。shell 变量中有一部分时环境变量，有一部分是局部变量，这些变量保证了 shell 的正常运行。

##### 2.5.Shell 字符串

字符串是 shell 编程中最常用的数据类型（只有数字和字符串），字符串可以使用单引号，双引号，甚至不用引号但可以。（但这并不意味着它们没有有区别）

**单引号**

- 单引号内任何字符都会原样输出，变量无效；
- 单引号中不能出现单独一个的单引号（对单引号使用转义字符也不行），只能成对出现，可以进行字符串拼接；

```shell
num=112
str='this ${num} \\n'

echo $str
# this ${num} \\n

# 字符串拼接
str1='this is '$num'!'

echo $str $str1
# this ${num} \\n this is 112!'
```

**双引号**

- 可以由变量；
- 可以有转义字符；

```shell
numS=113

strS="this ${numS} \\n"
echo $strS
# this 113 \n

strS1="this is "$numS"!"
echo $strS $strS1
# this 113 \n this is 113!

read -p "请输入" n
```

**不用引号**

- 只能用于单字符

```shell
# 不要引号
noStr=this is zhangsan
echo $noStr
# is: command not found

noStr=thisiszhangsan
echo $noStr
# thisiszhangsan
```

**获取字符串长度**

```shell
echo ${#noStr}
# 14
```

**提取字串**

```shell
echo ${noStr:0:6}
# thisis
```

**查找子串**

```shell
echo `expr index "$noStr" is`
# 3
```

##### 2.7.Shell 数组

支持一维数组（不支持多维数组），并且没有限定数组的大小。数组元素的下标由 0 开始编号。获取数组元素要利用下标，下标可以是整数或算术表达式（表达式的值大于或等于 0）。

**定义数组**

在 Shell 中，用括号来表示数组，数组元素用“空格”符号分开：

```shell
ary=(1 2 3)
# 或
ary[3]=4
```

> 可以不使用连续的下标，而且下标的范围没有限制。

**读取数组**

```shell
ary=(1 2 3)

# 错误用法，默认返回第一位
echo $ary # 1
echo ${ary} # 1

# 一般读取数组元素
echo ${ary[1]} # 2
echo ${ary[9]} # ''

# 获取全部数组元素
echo ${ary[@]} # 1 2 3
# 或
echo ${ary[*]} # 1 2 3
```

**数组长度**

```shell
echo ${#ary[@]} # 4
# 或
echo ${#ary[*]} # 4
```

##### 2.8.Shell 注释

**单行注释**

以 `#` 开头的行就是注释，会被解释器忽略。

```shell
#------------- start
# this is a comment
#------------- end
```

**多行注释**

```shell
:<<EOF
...
EOF

# 也可以使用其他符号

:<<!
...
!
```

参考：

1.[Shell 教程](https://www.runoob.com/linux/linux-shell.html)

2.[掌握Shell编程，一篇就够了](https://zhuanlan.zhihu.com/p/102176365)
