# EditorConfig

EditorConfig helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs. The EditorConfig project consists of a file format for defining coding styles and a collection of text editor plugins that enable editors to read the file format and adhere to defined styles. EditorConfig files are easily readable and they work nicely with version control systems.[^1]

Example file

```shell
# EditorConfig is awesome: https://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true

# Matches multiple files with brace expansion notation
# Set default charset
[*.{js,py}]
charset = utf-8

# 4 space indentation
[*.py]
indent_style = space
indent_size = 4

# Tab indentation (no size specified)
[Makefile]
indent_style = tab

# Indentation override for all JS under lib directory
[lib/**.js]
indent_style = space
indent_size = 2

# Matches the exact files either package.json or .travis.yml
[{package.json,.travis.yml}]
indent_style = space
indent_size = 2
```

## 通配符

在通配符匹配的部分名称中识别的特殊字符：

| characters     | descirbe                                                             |
| -------------- | -------------------------------------------------------------------- |
| `*`            | 匹配任何字符串，路径分隔符 (`/`) 除外                                |
| `**`           | 匹配任何字符串(包括路径分隔符)                                       |
| `?`            | 匹配任何单字符                                                       |
| `[name]`       | 匹配 `name` 中的任何单个字符                                         |
| `[!name]`      | 匹配非 `name` 中的任何单个字符                                       |
| `{s1,s2,s3}`   | 匹配任何给定的字符串（以逗号分隔）                                   |
| `{num1..num2}` | 匹配 `num1` 和 `num2` 之间的任何整数，其中 `num1` 和 `num2` 可以是正数或负数 |

> 特殊字符可以用反斜杠转义，这样它们就不会被解释为通配符模式。

## 可配置的属性

> 并非每个插件都支持所有[属性](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties)。

- `indent_style`:
  - `tab`
  - `space`

- `indent_size`:
  - an integer
  - `tab` (会使用 `tab_width` 的值)

- `tab_width`:
  - an integer (默认是 `indent_size` 的值，通常不需要指定)

- `end_of_line`:
  - `lf`
  - `cr`
  - `crlf`

- `charset`:
  - `latinl`
  - `utf-8`
  - `utf-8-bom`
  - `utf-16be`
  - `utf-16le`

- `trim_trailing_whitespece`:
  - `true` 删除换行符之前的任何空白字符
  - `false`

- `insert_final_newline`:
  - `true` 确保文件保存时以换行符结尾
  - `false`

- `root`: 应在任何部分之外的文件顶部指定的特殊属性
  - `true` 停止对当前文件的上层 `.editorconfig` 文件的搜索






---

参考：

[^1]:[EditorConfig](https://editorconfig.org/)

[^2]:[使用 EditorConfig 创建可移植的自定义编辑器设置](https://docs.microsoft.com/zh-cn/visualstudio/ide/create-portable-custom-editor-options?view=vs-2022)

[^3]:[统一代码风格工具——editorConfig](https://www.cnblogs.com/xiaohuochai/p/7160067.html)
