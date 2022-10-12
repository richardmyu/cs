# PowerShell

## 管理计算机

### 更改计算机状态

```shell
# 关闭计算机
Stop-Computer

# 重启操作系统
Restart-Computer

# 强制立即重新启动计算机
Restart-Computer -Force
```

## 管理驱动器与文件

> more [系统管理的示例脚本](https://docs.microsoft.com/zh-cn/powershell/scripting/samples/sample-scripts-for-administration?view=powershell-7.2)

### 管理当前位置

- **`Get-Location/Set-Location`**

```shell
Get-Alias -Definition Get-Location

# CommandType     Name                                               Version    Source
# -----------     ----                                               -------    ------
# Alias           gl -> Get-Location
# Alias           pwd -> Get-Location

Get-Alias -Definition Set-Location

# CommandType     Name                                               Version    Source
# -----------     ----                                               -------    ------
# Alias           cd -> Set-Location
# Alias           chdir -> Set-Location
# Alias           sl -> Set-Location

```

确定当前目录位置的路径/指定当前目录位置：

```shell
Get-Location
# Path
# ----
# C:\xxx\xx\xx

Set-Location -Path ..
```

> Get-Location cmdlet 类似于 BASH shell 中的 pwd 命令。 Set-Location cmdlet 类似于 Cmd.exe 中的 cd 命令。

### 使用文件和文件夹

#### 列出某个文件夹内的所有文件和文件夹

```shell
Get-Alias -Definition Get-ChildItem

# CommandType     Name                                               Version    Source
# -----------     ----                                               -------    ------
# Alias           dir -> Get-ChildItem
# Alias           gci -> Get-ChildItem
# Alias           ll -> Get-ChildItem

# 可选的 Force 参数以显示隐藏项或系统项
# 只列出直接包含的项，很像使用 Cmd.exe 的 DIR 命令或 UNIX shell 中的 ls
Get-ChildItem -Path . -Force

# 显示包含的项，还需要指定 -Recurse 参数
# -Recurse 可简写为 -r，但
# -Force 不可简写为 -f
Get-ChildItem -Path . -Force -Recurse
```

#### 复制文件和文件夹

```shell
Get-Alias -Definition Copy-Item

# CommandType     Name                                               Version    Source
# -----------     ----                                               -------    ------
# Alias           copy -> Copy-Item
# Alias           cp -> Copy-Item
# Alias           cpi -> Copy-Item

# 如果目标文件已存在，则复制尝试失败
Copy-Item -Path ./README.md -Destination ..

# 若要覆盖预先存在的目标，请使用 Force 参数
Copy-Item -Path ./README.md -Destination .. -Force

# 复制文件夹
Copy-Item ./docs -r ..
```

#### 创建文件和文件夹

```shell
Get-Alias -Definition New-Item

# CommandType     Name                                               Version    Source
# -----------     ----                                               -------    ------
# Alias           ni -> New-Item

# 新建文件夹
New-Item -Path 'xx/xx/folder-name' -ItemType Directory
# 当前目录新建
New-Item f-name -ItemType Directory

# 新建空的文件
New-Item -Path 'xx/xx/file-name.txt' -ItemType File
# 当前目录新建
New-Item f-name.txt  -ItemType File
# or
New-Item f-name.txt
```

#### 删除某个文件夹内的所有文件和文件夹

```shell
Get-Alias -Definition Remove-Item

# CommandType     Name                                               Version    Source
# -----------     ----                                               -------    ------
# Alias           del -> Remove-Item
# Alias           erase -> Remove-Item
# Alias           rd -> Remove-Item
# Alias           ri -> Remove-Item
# Alias           rm -> Remove-Item
# Alias           rmdir -> Remove-Item

# 删除文件
Remove-Item -Path file.txt

# 删除非空文件夹
Remove-Item -Path folder -Recurse
```

#### 将文本文件数据读取到数组中

```shell
Get-Alias -Definition Get-Content

# CommandType     Name                                               Version    Source
# -----------     ----                                               -------    ------
# Alias           cat -> Get-Content
# Alias           gc -> Get-Content
# Alias           type -> Get-Content

Get-Content -Path /xx/xx
# 当前目录
Get-Content file.txt
```

### 使用文件、文件夹和注册表项

- 枚举文件、文件夹和注册表项 (`Get-ChildItem`)

```shell
Get-ChildItem -Path xx/xx
```

- 列出所有包含的项 (`-Recurse`)

```shell
Get-ChildItem -Path xx/xx -Recrse
```

- 按名称筛选项 (`-Name`)

```shell
Get-ChildItem -Path xx/xx -Name
```

- 强制列出隐藏的项 (`-Force`)

```shell
Get-ChildItem -Path xx/xx -Force
```

#### 使用通配符匹配项名称

Windows PowerShell 通配符表示法包括：

- 星号 (`*`) 匹配零个或多个出现的任何字符。
- 问号 (`?`) 完全匹配一个字符。
- 左括号 (`[`) 字符和右括号 (`]`) 字符括起一组要匹配的字符。

```shell
Get-ChildItem -Path C:\Windows\?????.log
```

#### 排除项 (`-Exclude`)

```shell
Get-ChildItem -Path C:\WINDOWS\System32\w*32*.dll -Exclude win*
```
