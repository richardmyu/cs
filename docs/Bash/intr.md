# bash

### 运行

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
