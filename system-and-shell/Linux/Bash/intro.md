# Shell

Shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。Shell 既是一种命令语言，也是一种程序设计语言。

## Shell  脚本

Shell 脚本（Shell script），是一种为 Shell 编写的脚本程序。业界所说的 Shell 通常是指 Shell 脚本，但注意 Shell 和 Shell script 是两个不同的概念。

> 由于习惯原因，后文出现的 "Shell 编程" 都是指 Shell 脚本编程，而不是开发 Shell 自身。

## Shell 环境

Shell 编程跟 JavaScript、PHP 编程一样，只要有一个能写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。

Linux 的 Shell 种类繁多：

- Bourne Shell (usr/bin/sh 或 /bin/sh)
- Bourne Again Shell (/bin/bash)
- C Shell (/usr/bin/csh)
- K Shell (/usr/bin/ksh)
- Shell for Root (/sbin/sh)

一般情况下，并不区分 Bourne Shell 和 Bourne Again Shell，所以，像 `#!/bin/sh`，同样也可以改写为 `#!/bin/bash`。

> 但为了兼容不同系统，一般会用 `#!/usr/bin/env bash`。

`#!` ·告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序。

本笔记学习的是 Bash。（Bash 也是大多数 Linux 系统默认的 Shell）
