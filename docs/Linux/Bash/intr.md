# bash

### 1.运行

运行 Shell 脚本有两种方法：

**1.作为可执行程序**

```shell
chmod +x /path/hello.sh # 使脚本具有执行的权限
/path/hello.sh # 执行脚本
```

> 注意：是 `./hello.sh` 而不是 `hello.sh`。后者，Linux 系统会去 `PATH` 中寻找 `hello.sh`，而 `PATH` 中只有 `/bin`、`/sbin`、`/usr/bin` 等等，而当前目录通常不在 `PATH` 中，所以会找不到命令无法执行。`./hello.sh` 则是指明在当前目录查找。

**2.作为解释器参数**

直接运行解释器，其参数就是 Shell 脚本的文件名：

```shell
/bin/bash /path/hello.sh
/bin/zsh /path/hello.sh
bash /path/hello.sh

# or
source /path/hello.sh

# or
. /path/hello.sh

# 实际测试中，以下这种也可以
/path/hello.sh
```

> 这种方式运行脚本，不需要在第一行指定解释器（写了也没用）。



脚本也可以在 windows 的 power shell 中运行，但是需要先安装 Git，本质是调用 Git 来执行脚本。当然执行完后会自动关闭 Git 。

```shell
# 第一种：直接运行，需要调用 Git
./hello.sh

# 第二种：输入 bash 命令进入 bash 模式
> bash
> sh hello.sh
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
c_class="abc"
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
# abc = efg: c_class 不等于 g
# abc != efg : c_class 不等于 g
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

### 5.echo 命令

Shell 的 `echo` 指令用于字符串的输出。命令格式：

```shell
echo string
```

**1.显示普通字符串**

```shell
echo "It is a test"
# 或
echo It is a test

# It is a test
```

**2.显示转义字符**

```shell
echo "\"It is a test\""
# 或
echo \"It is a test\"

# "It is a test"
```

**3.显示变量**

```shell
name=Jack
echo "$name, it is a test."

# jack, it is a test.
```

**4.显示换行**


```shell
echo -e "OK!\n" # -e 开启转义
echo "It is a jock"

# OK!
#
# It is a jock
```

**5.显示不换行**


```shell
echo -e "OK! \c" # \c_class 不换行
echo "It is a jock"

# OK! It is a jock
```

**6.显示结果定向至文件**

```shell
echo "It is a test" > test.log.md
```

> 若文件不存在，则会自动创建。

**7.原样输出字符串，不进行转义或取变量(用单引号)**

```shell
echo -e '$name\"'

# $name\"
```

**8.显示命令执行结果**

```shell
echo `date`

# 2020年11月30日, 周一 22:31:26
```

> 注意： 这里使用的是反引号 `, 而不是单引号 '。

### 6.printf 命令

`printf` 命令模仿 C 程序库（library）里的 `printf()` 程序。

`printf` 由 POSIX 标准所定义，因此使用 `printf` 的脚本比使用 `echo` 移植性好。

`printf` 使用引用文本或空格分隔的参数，外面可以在 `printf` 中使用格式化字符串，还可以制定字符串的宽度、左右对齐方式等。默认 `printf` 不会像 `echo` 自动添加换行符，我们可以手动添加 `\n`。

`printf` 命令的语法：

```shell
printf  format-string  [arguments...]
```

参数说明：

- `format-string`: 为格式控制字符串
- `arguments`: 为参数列表。

```shell
echo "hello,world"
# 等效
printf "hello,world\n"
```

接下来,用一个脚本来体现 `printf` 的强大功能：

```shell
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" 张三 男 66.1234
printf "%-10s %-8s %-4.2f\n" 王五 男 48.6543
printf "%-10s %-8s %-4.2f\n" 李思 女 47.9876
```

执行脚本，输出结果如下所示：

```shell
# 姓名     性别   体重kg
# 张三     男      66.12
# 王五     男      48.65
# 李思     女      47.99
```

> `%s`、`%c`、`%d`、`%f` 都是格式替代符。

`%-10s` 指一个宽度为 10 个字符（`-` 表示左对齐，没有则表示右对齐），任何字符都会被显示在 10 个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。

`%-4.2f` 指格式化为小数，其中 `.2` 指保留 2 位小数。

```shell
# format-string 为双引号
printf "%d %s\n" 1 "abc"
# 1 abc

# 单引号与双引号效果一样
printf '%d %s\n' 1 "abc"
# 1 abc

# 没有引号也可以输出
printf %s abcdef
# abcdef


# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
printf %s abc def
# abcdef


printf "%s\n" abc def
# abc
# def

printf "%s %s %s\n" a b c_class d e f g h i j
# a b c_class
# d e f
# g h i
# j


# 如果没有 arguments，那么
# %s 用 NULL 代替
# %d 用 0 代替
# %c_class 用 NULL 代替
# %f 用 0.000000 代替
printf "%s and %d and %c and %f \n"
# and 0 and  and 0.000000
```

**printf 的转义序列**

| 序列    | 说明                                                                                                                                                                         |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `\a`    | 警告字符，通常为ASCII的BEL字符                                                                                                                                               |
| `\b`    | 后退                                                                                                                                                                         |
| `\c`    | 抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效），而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略 |
| `\f`    | 换页                                                                                                                                                                         |
| `\n`    | 换行                                                                                                                                                                         |
| `\r`    | 回车                                                                                                                                                                         |
| `\t`    | 水平制表符                                                                                                                                                                   |
| `\v`    | 垂直制表符                                                                                                                                                                   |
| `\\`    | 一个字面上的反斜杠字符                                                                                                                                                       |
| `\ddd`  | 表示1到3位数八进制值的字符。仅在格式字符串中有效                                                                                                                             |
| `\0ddd` | 表示1到3位的八进制值字符                                                                                                                                                     |

### 7.test 命令

Shell 中的 `test` 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

**1.数值测试**

| 参数  | 说明           |
| ----- | -------------- |
| `-eq` | 等于则为真     |
| `-ne` | 不等于则为真   |
| `-gt` | 大于则为真     |
| `-ge` | 大于等于则为真 |
| `lt`  | 小于则为真     |
| `le`  | 小于等于则为真 |


```shell
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

# 两个数相等！
# result 为： 200
```

> 代码中的 `[]` 执行基本的算数运算（不需要前后空格）

**2.字符串测试**

| 参数 | 说明                     |
| ---- | ------------------------ |
| `=`  | 等于则为真               |
| `!=` | 不相等则为真             |
| `-z` | 字符串的长度为零则为真   |
| `-n` | 字符串的长度不为零则为真 |

```shell
str1="ru1noob"
str2="runoob"
if test $str1 = $str2
then
    echo '两个字符串相等!'
else
    echo '两个字符串不相等!'
fi

# 两个字符串不相等!
```

**3.文件测试**

| 参数 | 说明                                 |
| ---- | ------------------------------------ |
| `-e` | 如果文件存在则为真                   |
| `-r` | 如果文件存在且可读则为真             |
| `-w` | 如果文件存在且可写则为真             |
| `-x` | 如果文件存在且可执行则为真           |
| `-s` | 如果文件存在且至少有一个字符则为真   |
| `-d` | 如果文件存在且为目录则为真           |
| `-f` | 如果文件存在且为普通文件则为真       |
| `-c` | 如果文件存在且为字符型特殊文件则为真 |
| `-b` | 如果文件存在且为块特殊文件则为真     |

```shell
cd /bin
if test -e ./bash
then
    echo '文件已存在!'
else
    echo '文件不存在!'
fi

# 文件已存在!
```

另外，Shell 还提供了与(`-a`)、或(`-o`)、非(`!`)三个逻辑操作符用于将测试条件连接起来，其优先级为： `!` 最高， `-a` 次之， `-o` 最低。例如：

```shell
cd /bin
if test -e ./notFile -o -e ./bash
then
    echo '至少有一个文件存在!'
else
    echo '两个文件都不存在'
fi

# 至少有一个文件存在!
```

### 8.流程控制

##### 8.1.if 语句

Shell 的流程控制不可为空。如果 `else` 分支没有语句执行，就不要写这个 `else`。

```shell
# if
if condition
then
    command
    ...
fi
# or (一行，适用于终端)
if condition;then command; fi


# if-else
if condition
then
    command
    ...
else
    command
if

# if-elsf-else(if-elif...-else)
if condition
then
    command
    ...
elif condition
then
    command
else
    command
fi
```

##### 8.2.for 循环

or循环一般格式为：

```shell
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done

# 写成一行
for i in item1 item2 ... itemN; do command ...; done;
```

当变量值在列表里，`for` 循环即执行一次所有命令，使用变量名获取列表中的当前取值。命令可为任何有效的 shell 命令和语句。`in` 列表可以包含替换、字符串和文件名。

`in` 列表是可选的，如果不用它，`for` 循环使用命令行的位置参数。

```shell
for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done

# The value is: 1
# The value is: 2
# The value is: 3
# The value is: 4
# The value is: 5
```

##### 8.3.while 语句

`while` 循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件。其格式为：

```shell
while condition
do
    command
done
```

以下是一个基本的 `while` 循环：

```shell
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done

# 1
# 2
# 3
# 4
# 5
```

以上实例使用了 Bash `let` 命令，它用于执行一个或多个表达式，变量计算中不需要加上 `$` 来表示变量，具体可查阅：[Bash `let` 命令](https://www.runoob.com/linux/linux-comm-let.html)。

**无限循环**

```shell
while :
do
    command
done

# or
while true
do
    command
done

# or
for (( ; ; ))
```

##### 8.4.until 循环

`until` 循环执行一系列命令直至条件为 true 时停止。

`until` 循环与 `while` 循环在处理方式上刚好相反。

一般 `while` 循环优于 `until` 循环，但在某些时候—也只是极少数情况下，`until` 循环更加有用。

```shell
# until 语法格式
until condition
do
    command
done
```

`condition` 一般为条件表达式，如果返回值为 false，则继续执行循环体内的语句，否则跳出循环。

```shell
a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

##### 8.5.case

`case ... esac` 与其他语言中的 `switch ... case` 语句类似，是一种多分枝选择结构，每个 `case` 分支用右圆括号开始，用两个分号 `;;` 表示 `break`，即执行结束，跳出整个 `case ... esac` 语句，`esac`（就是 `case` 反过来）作为结束标记。

```shell
case 值 in
模式1) # 右括号结束模式
    command1
    command2
    ...
    commandN
    ;; # ;; 标记单个模式结束
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
```

`case` 后为取值，取值可以为变量或常数。

取值后面必须为单词 `in`，每一模式必须以右括号结束。

取值将检测匹配的每一个模式。一旦模式匹配，其间所有命令开始执行直至 `;;`，并且执行完匹配模式相应命令后不再继续其他模式。

如果无一匹配模式，使用星号 `*` 捕获该值，再执行后面的命令。

```shell
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
1)
    echo '你选择了 1'
    ;;
2)
    echo '你选择了 2'
    ;;
3)
    echo '你选择了 3'
    ;;
4)
    echo '你选择了 4'
    ;;
*)
    echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

##### 8.6.跳出循环

在循环过程中，有时候需要在未达到循环结束条件时强制跳出循环，Shell 使用两个命令来实现该功能：`break` 和 `continue`。

**1.break**

`break` 命令允许跳出所有循环（终止执行后面的所有循环）。

```shell
while :
do
    echo -n "输入 1 到 5 之间的数字:"
    read aNum
    case $aNum in
    1|2|3|4|5)
        echo "你输入的数字为 $aNum!"
        ;;
    *)
        echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
            break
            echo "游戏结束" # 会被执行
        ;;
    esac
done
```

**2.continue**

`continue` 命令与 `break` 命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

```shell
while :
do
    echo -n "输入 1 到 5 之间的数字: "
    read aNum
    case $aNum in
    1|2|3|4|5)
        echo "你输入的数字为 $aNum!"
        ;;
    *)
        echo "你输入的数字不是 1 到 5 之间的!"
            continue
            echo "游戏结束" # 不会被执行
        ;;
    esac
done
```


### 9.函数

shell 可以用户定义函数，然后在 shell 脚本中可以随便调用。

shell 中函数的定义格式如下：

```shell
[ function ] funname [()]

{
    action;

    [return int;]

}
```

说明：

1. 可以带 `function fun()` 定义，也可以直接 `fun()` 定义,不带任何参数。
2. 参数返回，可以显示加：`return` 返回，如果不加，将以最后一条命令运行结果，作为返回值。`return` 后跟数值 n(0-255)。

```shell
sayHello(){
  echo "Hello!"
}
# 调用函数
sayHello

# 带 return
funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
```



> 注意：所有函数在使用前必须定义。这意味着必须将函数放在脚本开始部分，直至 shell 解释器首次发现它时，才可以使用。调用函数仅使用其函数名即可。
> 函数返回值在调用该函数后通过 `$?` 来获得。在函数执行前，执行获取函数返回值的操作不会出错(大概无法排除是为了获取上一个)，但是得不到结果，并且 `$?` 只会在函数调用后第一次调用且没有进行其他操作或命令才能取道函数的返回值。(`$?` 仅对其上一条指令负责，一旦函数返回后其返回值没有立即保存入参数，那么其返回值将不再能通过 `$?` 获得。)

**1.函数参数**

在 Shell 中，调用函数时可以向其传递参数。在函数体内部，通过 `$n` 的形式来获取参数的值：

```shell
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73

# 第一个参数为 1 !
# 第二个参数为 2 !
# 第十个参数为 10 !
# 第十个参数为 34 !
# 第十一个参数为 73 !
# 参数总数有 11 个!
# 作为一个字符串输出所有参数 1 2 3 4 5 6 7 8 9 34 73 !
```

> 注意，`$10` 不能获取第十个参数，获取第十个参数需要 `${10}`。当 `n>=10` 时，需要使用 `${n}` 来获取参数。

### 10.输入/输出重定向

大多数 UNIX 系统命令从你的终端接受输入并将所产生的输出发送回​​到您的终端。一个命令通常从一个叫标准输入的地方读取输入，默认情况下，这恰好是你的终端。同样，一个命令通常将其输出写入到标准输出，默认情况下，这也是你的终端。

| 命令              | 说明                                               |
| ----------------- | -------------------------------------------------- |
| `command > file`  | 将输出重定向到 file。                              |
| `command < file`  | 将输入重定向到 file。                              |
| `command >> file` | 将输出以追加的方式重定向到 file。                  |
| `n > file`        | 将文件描述符为 n 的文件重定向到 file。             |
| `n >> file`       | 将文件描述符为 n 的文件以追加的方式重定向到 file。 |
| `n >& m`          | 将输出文件 m 和 n 合并。                           |
| `n <& m`          | 将输入文件 m 和 n 合并。                           |
| `<< tag`          | 将开始标记 tag 和结束标记 tag 之间的内容作为输入。 |

> 需要注意的是文件描述符 0 通常是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。

**1.输出重定向**

重定向一般通过在命令间插入特定的符号来实现。特别的，这些符号的语法如下所示:

```shell
command1 > file1
```

注意任何 `file1` 内的已经存在的内容将被新内容替代。如果要将新内容添加在文件末尾，请使用 `>>` 操作符。

执行下面的 `who` 命令，它将命令的完整的输出重定向在用户文件中(users):

```shell
$ who > users
```

执行后，并没有在终端输出信息，这是因为输出已被从默认的标准输出设备（终端）重定向到指定的文件。

你可以使用 `cat` 命令查看文件内容：

```shell
$ cat users
#
```

输出重定向会覆盖文件内容：

```shell
$ echo "瓜瓜" > users
$ cat users
瓜瓜
$
```

如果不希望文件内容被覆盖，可以使用 `>>` 追加到文件末尾：

```shell
$ echo "嘎嘎" >> users
$ cat users
瓜瓜
嘎嘎
$
```

**2.输入重定向**

和输出重定向一样，Unix 命令也可以从文件获取输入，语法为：

```shell
command1 < file1
```

这样，本来需要从键盘获取输入的命令会转移到文件读取内容。

> 注意：输出重定向是大于号(`>`)，输入重定向是小于号(`<`)。

接着以上实例，我们需要统计 `users` 文件的行数,执行以下命令：

```shell
$ wc -l users
       2 users
```

也可以将输入重定向到 `users` 文件：

```shell
$  wc -l < users
       2
```

注意：上面两个例子的结果不同：第一个例子，会输出文件名；第二个不会，因为它仅仅知道从标准输入读取内容。

```shell
command1 < infile > outfile
```

同时替换输入和输出，执行 `command1`，从文件 `infile` 读取内容，然后将输出写入到 `outfile` 中。

**重定向深入讲解**

一般情况下，每个 Unix/Linux 命令运行时都会打开三个文件：

- 标准输入文件(stdin)：`stdin` 的文件描述符为 0，Unix 程序默认从 `stdin` 读取数据。
- 标准输出文件(stdout)：`stdout` 的文件描述符为 1，Unix 程序默认向 `stdout` 输出数据。
- 标准错误文件(stderr)：`stderr` 的文件描述符为 2，Unix 程序会向 `stderr` 流中写入错误信息。

默认情况下，`command > file` 将 `stdout` 重定向到 `file`，`command < file` 将 `stdin` 重定向到 `file`。

如果希望 `stderr` 重定向到 `file`，可以这样写：

```shell
$ command 2>file
```

如果希望 `stderr` 追加到 `file` 文件末尾，可以这样写：

```shell
$ command 2>>file
```

如果希望将 `stdout` 和 `stderr` 合并后重定向到 `file`，可以这样写：

```shell
$ command > file 2>&1
```

或者

```shell
$ command >> file 2>&1
```

如果希望对 `stdin` 和 `stdout` 都重定向，可以这样写：

```shell
$ command < file1 >file2
```

`command` 命令将 `stdin` 重定向到 `file1`，将 `stdout` 重定向到 `file2`。

**3.Here Document**

Here Document 是 Shell 中的一种特殊的重定向方式，用来将输入重定向到一个交互式 Shell 脚本或程序。

```shell
command << delimiter
    document
delimiter
```

它的作用是将两个 `delimiter` 之间的内容(document) 作为输入传递给 `command`。

> 注意：
>
>> 结尾的 `delimiter` 一定要顶格写，前面不能有任何字符，后面也不能有任何字符，包括空格和 tab 缩进。
>> 开始的 `delimiter` 前后的空格会被忽略掉。

在命令行中通过 `wc -l` 命令计算 Here Document 的行数：

```shell
# 命令行中着这么个样子
$ wc -l << EOF
> 瓜瓜
> 嘎嘎
> 哈哈哈
> EOF
3          # 输出结果为 3 行
$
```

我们也可以将 Here Document 用在脚本中，例如：

```shell
cat << EOF
嘎嘎
瓜瓜
略略略
EOF
```

**4./dev/null 文件**

如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到  `/dev/null`：

```shell
$ command > /dev/null
```

`/dev/null` 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 `/dev/null` 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 `stdout` 和 `stderr`，可以这样写：

```shell
$ command > /dev/null 2>&1
```

> 注意：0 是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。这里的 2 和 `>` 之间不可以有空格，`2>` 是一体的时候才表示错误输出。

### 11.文件包含

和其他语言一样，Shell 也可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。

Shell 文件包含的语法格式如下：

```shell
. filename   # 注意点号(.)和文件名中间有一空格

# 或
source filename
```

创建两个 shell 脚本文件。

`file1.sh` 代码如下：

```shell

url="http://www.runoob.com"
```

`file2.sh` 代码如下：

```shell
#使用 . 号来引用 file1.sh 文件
. ./file1.sh

# 或者使用以下包含文件代码
# source ./file1.sh

echo "菜鸟教程官网地址：$url"
```

接下来执行：

```shell
$ ./file2.sh

# 菜鸟教程官网地址：http://www.runoob.com
```

> 注：但被包含的文件 `file1.sh` 不需要可执行权限。

参考：

1.[Shell 教程](https://www.runoob.com/linux/linux-shell.html)

2.[掌握Shell编程，一篇就够了](https://zhuanlan.zhihu.com/p/102176365)

3.[Shell 编程范例](https://tinylab.gitbooks.io/shellbook/content/)
