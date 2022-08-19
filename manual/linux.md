# Linux

## 1.查看

### 1.1.查看内存

#### 1.1.1.`/proc/meminfo`

查看 RAM 使用情况最简单的办法就是通过 `/proc/meminfo`。这个动态更新的虚拟文件实际上是许多其他内存相关工具（如：free / ps / top）等的组合显示。`/proc/meminfo` 列出了所有你想了解的内存的使用情况。进程的内存使用信息也可以通过 `/proc/<pid>/statm` 和 `/proc/<pid>/status` 来查看。

```shell
$ cat /proc/meminfo
MemTotal:       16210664 kB
MemFree:         3051372 kB
MemAvailable:    9934544 kB
Buffers:         1529276 kB
Cached:          5430752 kB
# ...
```

#### 1.1.2.`atop`

`atop` 命令是一个终端环境的监控命令。它显示的是各种系统资源（CPU, memory, network, I/O, kernel）的综合，并且在高负载的情况下进行了彩色标注。

```shell
# atop 需要预先安装
atop
```

#### 1.1.3.`free`

`free` 是一个快速查看内存使用情况的方法，是对 `/proc/meminfo` 收集到的信息的一个概述。

```shell
free -h

              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.4Gi       2.7Gi       1.3Gi       8.3Gi       9.4Gi
Swap:          15Gi       2.0Mi        15Gi
```

#### 1.1.4.`gnome-system-monitor`

`gnome-system-monitor` 是一个显示最近一段时间内的 CPU、内存、交换区及网络的使用情况的视图工具。它还提供了一种查看 CPU 及内存使用情况的方法。

```shell
gnome-system-monitor
```

#### 1.1.5.`htop`

`htop` 命令显示了每个进程的内存实时使用率。它提供了所有进程的常住内存大小、程序总内存大小、共享库大小等的报告。

```shell
# htop 需要预先安装
htop
```

#### 1.1.6.`top`

`top` 命令提供了实时的运行中的程序的资源使用统计。

```shell
top
```

#### 1.1.7.`ps`

`ps` 命令可以实时的显示各个进程的内存使用情况。

```shell
ps

ps aux --sort -rss
```

#### 1.1.8.`vmstat`

`vmstat` 命令显示实时的和平均的统计，覆盖 CPU、内存、I/O 等内容。

```shell
vmstat -s
```
