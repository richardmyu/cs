# Linux

## 1.查看

### 1.1.查看内存

#### 1.1.1.`/proc/meminfo`

查看 RAM 使用情况最简单的办法就是通过 `/proc/meminfo`。这个动态更新的虚拟文件实际上是许多其他内存相关工具（如：free / ps / top）等的组合显示。`/proc/meminfo` 列出了所有你想了解的内存的使用情况。进程的内存使用信息也可以通过 `/proc/<pid>/statm` 和 `/proc/<pid>/status` 来查看。

```shell

```
