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

### 1.2.监控日志文件

一般来说，所有的日志文件都位于 `/var/log`。此目录包含特定应用和服务的拓展名为 `.log` 的日志文件，它还包含了其他含有日志独立目录。

#### 1.2.1.`tail`

`tail` 命令是实时跟踪日志文件的最基本方式。

```shell
# 使用开关 -f 跟踪实时更新的日志文件
tail -f /var/log/syslog

# 监控多个
tail -f /var/log/syslog /var/log/dmesg
```

> `lnav` 可以使用彩色编码的信息以更条理的方式监控日志文件。

#### 1.2.2.`journalctl`

当今所有现代 linux 发行版都主要使用 `systemd`。`systemd` 提供了运行 linux 操作系统的基本框架和组建。 `systemd` 通过 `journalctl` 提供日志服务，这有助于管理来自所有 `systemd` 服务的日志。

```sh
journalctl -f

# 紧急系统消息
journalctl -p 0

# 带有解释的错误
journalctl -xb -p 0

# 时间过滤
journalctl --since "2022-12-12 06:00:00"
journalctl --since "2022-12-12" --until "2022-12-14 06:00:00"
journalctl --since yesterday
journalctl --since 09:00 --until "1 hour ago"
```
