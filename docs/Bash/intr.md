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

# 获取全部数组元素 @ 或 *
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

### 3.传递参数

我们可以在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：`$n`。n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……

以下实例我们向脚本传递三个参数，并分别输出，其中 `$0` 为执行的文件名（包含文件路径）：

```shell
#!/bin/bash
echo "Shell 传递参数实例！"
echo "执行的文件名：$0"
echo "第一个参数为：$1"
echo "第二个参数为：$2"
echo "第三个参数为：$3"
```

并执行脚本，输出结果如下所示：

```shell
Shell 传递参数实例！
执行的文件名：D:\..\bash\arg.sh
第一个参数为：1
第二个参数为：2
第三个参数为：3
```

另外，还有几个特殊字符用来处理参数：

| 参数 | 说明                                                           |
| ---- | -------------------------------------------------------------- |
| `$#` | 传递到脚本的参数个数                                           |
| `$*` | 以一个单字符显示所有向脚本传递的参数                           |
| `$@` | 显示全部参数                                                   |
| `$$` | 脚本运行的当前进程 ID 号                                       |
| `$!` | 后台运行的最后一个进程的 ID 号                                 |
| `$-` | 显示 Shell 使用的当前选项，与 `set` 命令功能相同               |
| `$?` | 显示最后命令的退出状态（0 表示没有错误，其他任何值表面有错误） |

`$*` 与 `$@` 区别：

- 相同点：都是引用所有参数。
- 不同点：只有在双引号中体现出来。假设在脚本运行时写了三个参数 1、2、3，则 "`*`" 等价于 "1 2 3"（传递了一个参数），而 "`@`" 等价于 "1" "2" "3"（传递了三个参数）。

```shell
echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
```

执行脚本，输出结果如下所示：

```shell
# -- $* 演示 ---
# 1 2 3
# -- $@ 演示 ---
# 1
# 2
# 3
# -------
```

> 在为 shell 脚本传递的参数中如果包含空格，应该使用单引号或者双引号将该参数括起来，以便于脚本将这个参数作为整体来接收。

### 4.运算符

Shell 和其他编程语言一样，支持多种运算符，包括：

- 算数运算符
- 关系运算符
- 布尔运算符
- 字符串运算符
- 文件测试运算符

原生 bash 不支持简单的数学运算，但是可以通过其他命令来实现，例如 `awk` 和 `expr`，`expr` 最常用。

`expr` 是一款表达式计算工具，使用它能完成表达式的求值操作：

```shell
res=`expr 2 + 2`
echo "和：$res"
```

两点注意：

- 表达式和运算符之间要有空格，例如 `2+2` 是不对的，必须写成 `2 + 2`，这与我们熟悉的大多数编程语言不一样。
- 完整的表达式要被 `` 包含。

**1.算术运算符**

| 运算符 | 说明                                          |
| ------ | --------------------------------------------- |
| `+`    | 加法                                          |
| `-`    | 减法                                          |
| `*`    | 乘法                                          |
| `/`    | 除法                                          |
| `%`    | 取余                                          |
| `=`    | 赋值                                          |
| `==`   | 相等（用于比较两个数字，相同则返回 true）     |
| `!=`   | 不相等（用于比较两个数字，不相同则返回 true） |

算术运算符实例如下：

```shell
a=7
b=8

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
   echo "a 等于 b"
fi

if [ $a != $b ]
then
   echo "a 不等于 b"
fi
```

>注意：条件表达式要放在方括号之间，并且要有空格，例如: `[$a==$b]` 是错误的，必须写成 `[ $a == $b ]`。

执行脚本，输出结果如下所示：

```shell
# a + b : 15
# a - b : -1
# a * b : 56
# b / a : 1
# b % a : 1
# a 不等于 b
```

注意：

- 乘号(`*`)前边必须加反斜杠(`\`)才能实现乘法运算；
- `if...then...fi` 是条件语句。
- 在 MAC 中 shell 的 `expr` 语法是：`$((表达式))`，此处表达式中的 "`*`" 不需要转义符号 "`\`" 。
- 赋值（`=`）操作不仅不跟其他运算符一样前后空一格，并且是前后都不能空一格。

**2.关系运算符**

关系运算符只支持数字，不支持字符串，除非字符串的值是数字。

| 运算符 | 说明                                                  | 注释 |
| ------ | ----------------------------------------------------- | ---- |
| `eq`   | 检测两个数是否相等，相等返回 true。                   | `=`  |
| `ne`   | 检测两个数是否不相等，不相等返回 true。               | `!=` |
| `gt`   | 检测左边的数是否大于右边的，如果是，则返回 true。     | `>`  |
| `lt`   | 检测左边的数是否小于右边的，如果是，则返回 true。     | `<`  |
| `ge`   | 检测左边的数是否大于等于右边的，如果是，则返回 true。 | `>=` |
| `le`   | 检测左边的数是否小于等于右边的，如果是，则返回 true。 | `<=` |

关系运算符实例如下：

```shell
# 检测两个数是否相等，相等返回 true
if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi

# 检测两个数是否不相等，不相等返回 true
if [ $a -ne $b ]
then
   echo "$a -ne $b: a 不等于 b"
else
   echo "$a -ne $b : a 等于 b"
fi

# 检测左边的数是否大于右边的，如果是，则返回 true
if [ $a -gt $b ]
then
   echo "$a -gt $b: a 大于 b"
else
   echo "$a -gt $b: a 不大于 b"
fi

# 检测左边的数是否小于右边的，如果是，则返回 true
if [ $a -lt $b ]
then
   echo "$a -lt $b: a 小于 b"
else
   echo "$a -lt $b: a 不小于 b"
fi

# 检测左边的数是否大于等于右边的，如果是，则返回 true
if [ $a -ge $b ]
then
   echo "$a -ge $b: a 大于或等于 b"
else
   echo "$a -ge $b: a 小于 b"
fi

# 检测左边的数是否小于等于右边的，如果是，则返回 true
if [ $a -le $b ]
then
   echo "$a -le $b: a 小于或等于 b"
else
   echo "$a -le $b: a 大于 b"
fi
```

执行脚本，输出结果如下所示：

```shell
# 7 -eq 8: a 不等于 b
# 7 -ne 8: a 不等于 b
# 7 -gt 8: a 不大于 b
# 7 -lt 8: a 小于 b
# 7 -ge 8: a 小于 b
# 7 -le 8: a 小于或等于 b
```

**3.布尔运算符**

| 运算符 | 说明                                                |
| ------ | --------------------------------------------------- |
| `!`    | 非运算，表达式为 true 则返回 false，否则返回 true。 |
| `-o`   | 或运算，有一个表达式为 true 则返回 true。           |
| `-a`   | 与运算，两个表达式都为 true 才返回 true。           |

```shell
if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a == $b: a 等于 b"
fi

if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a 小于 100 且 $b 大于 15 : 返回 true"
else
   echo "$a 小于 100 且 $b 大于 15 : 返回 false"
fi

if [ $a -lt 100 -o $b -gt 100 ]
then
   echo "$a 小于 100 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 100 或 $b 大于 100 : 返回 false"
fi
```

执行脚本，输出结果如下所示：

```shell
# 7 != 8 : a 不等于 b
# 7 小于 100 且 8 大于 15 : 返回 false
# 7 小于 100 或 8 大于 100 : 返回 true
```

**4.逻辑运算符**

| 运算符 | 说明       |
| ------ | ---------- |
| `&&`   | 逻辑的 AND |
| `||`   | 逻辑的 OR  |

```shell
if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi

if [[ $a -lt 100 || $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi
```

执行脚本，输出结果如下所示：

```shell
# 返回 false
# 返回 true
```

**5.字符串运算符**

| 运算符 | 说明                                         |
| ------ | -------------------------------------------- |
| `=`    | 检测两个字符串是否相等，相等返回 true。      |
| `!=`   | 检测两个字符串是否相等，不相等返回 true。    |
| `-z`   | 检测字符串长度是否为 0，为0返回 true。       |
| `-n`   | 检测字符串长度是否不为 0，不为 0 返回 true。 |
| `$`    | 检测字符串是否为空，不为空返回 true。        |


```shell
c="abc"
g="efg"

if [ $c = $g ]
then
   echo "$c = $g : c 等于 g"
else
   echo "$c = $g: c 不等于 g"
fi
if [ $c != $g ]
then
   echo "$c != $g : c 不等于 g"
else
   echo "$c != $g: c 等于 g"
fi
if [ -z $c ]
then
   echo "-z $c : 字符串长度为 0"
else
   echo "-z $c : 字符串长度不为 0"
fi
if [ -n "$c" ]
then
   echo "-n $c : 字符串长度不为 0"
else
   echo "-n $c : 字符串长度为 0"
fi
if [ $c ]
then
   echo "$c : 字符串不为空"
else
   echo "$c : 字符串为空"
fi
````

执行脚本，输出结果如下所示：

```shell
# abc = efg: c 不等于 g
# abc != efg : c 不等于 g
# -z abc : 字符串长度不为 0
# -n abc : 字符串长度不为 0
# abc : 字符串不为空
```

**6.文件测试运算符**

| 操作符    | 说明                                                                        |
| --------- | --------------------------------------------------------------------------- |
| `-b file` | 检测文件是否是块设备文件，如果是，则返回 true。                             |
| `-c file` | 检测文件是否是字符设备文件，如果是，则返回 true。                           |
| `-d file` | 检测文件是否是目录，如果是，则返回 true。                                   |
| `-f file` | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 |
| `-g file` | 检测文件是否设置了 SGID 位，如果是，则返回 true。                           |
| `-k file` | 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。                 |
| `-p file` | 检测文件是否是有名管道，如果是，则返回 true。                               |
| `-u file` | 检测文件是否设置了 SUID 位，如果是，则返回 true。                           |
| `-r file` | 检测文件是否可读，如果是，则返回 true。                                     |
| `-w file` | 检测文件是否可写，如果是，则返回 true。                                     |
| `-x file` | 检测文件是否可执行，如果是，则返回 true。                                   |
| `-s file` | 检测文件是否为空（文件大小是否大于0），不为空返回 true。                    |
| `-e file` | 检测文件（包括目录）是否存在，如果是，则返回 true。                         |
| `-S file` | 判断某文件是否 socket，如果是，则返回 true。                                |
| `-L file` | 测文件是否存在并且是一个符号链接，如果是，则返回 true。                     |

```shell
file="./hello.sh"

if [ -r $file ]
then
   echo "文件可读"
else
   echo "文件不可读"
fi

if [ -w $file ]
then
   echo "文件可写"
else
   echo "文件不可写"
fi

if [ -x $file ]
then
   echo "文件可执行"
else
   echo "文件不可执行"
fi

if [ -f $file ]
then
   echo "文件为普通文件"
else
   echo "文件为特殊文件"
fi

if [ -d $file ]
then
   echo "文件是个目录"
else
   echo "文件不是个目录"
fi

if [ -s $file ]
then
   echo "文件不为空"
else
   echo "文件为空"
fi

if [ -e $file ]
then
   echo "文件存在"
else
   echo "文件不存在"
fi
```

执行脚本，输出结果如下所示：

```shell
# 文件可读
# 文件可写
# 文件可执行
# 文件为普通文件
# 文件不是个目录
# 文件不为空
# 文件存在
```

参考：

1.[Shell 教程](https://www.runoob.com/linux/linux-shell.html)

2.[掌握Shell编程，一篇就够了](https://zhuanlan.zhihu.com/p/102176365)
