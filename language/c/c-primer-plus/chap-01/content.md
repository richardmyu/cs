# 初始 C 语言

## 1. 编程机制

用 C 语言编写程序时，编写的内容被储存在文本文件中，该文件被称为 **源代码文件**（*source code file*）。大部分 C 系统，都要求文件以 `.c` 结尾。在文件名中，点号（`.`）前面的部分被称为 **基本名**（*basename*），点号后面的部分被称为 **扩展名**（*extension*）。

### 1.1. 目标代码文件、可执行文件和库

C 编程的基本策略是，用程序把源代码文件转换为成可执行文件（其中包含可直接运行的机器语言代码）。典型的 C 实现通过编译和链接两个步骤来完成这一个过程。

编译器把源代码转换成中间代码，链接器把中间代码和其他代码合并，生成可执行文件。C 使用这种分而治之的方法方便对程序进行模块化，可以独立编译单独的模块，稍后再用链接器合并已编译的模块。通过这种方式，如果只更改某个模块，不必因此重新编译其他模块。

中间文件有多种形式。这里描述的是最普遍的一种形式，鸡巴源代码转换为机器语言代码，并把结果放在 **目标代码文件**（或简称 目标文件）中。虽然目标文件中包含机器语言代码，但是并不能直接运行该文件。因为目标文件中存储的是编译器翻译的源代码，这还不是一个完整的程序。

目标代码文件缺失 **启动代码**（*startup code*）。启动代码充当着程序和操作系统之间的接口。

目标代码文件还缺少库函数。几乎所有的 C 程序都要使用 C 标准库中的函数。

链接器的作用是，把目标代码、系统的标准启动代码和库代码这 3 部分合并成一个文件，即可执行文件。对于库代码，链接器只会把程序中要用到的库函数代码提取出来。
