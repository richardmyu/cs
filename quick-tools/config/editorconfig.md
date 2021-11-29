# editorconfig

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

---

参考：

1.[EditorConfig](https://editorconfig.org/)
2.[使用 EditorConfig 创建可移植的自定义编辑器设置](https://docs.microsoft.com/zh-cn/visualstudio/ide/create-portable-custom-editor-options?view=vs-2022)
3.[统一代码风格工具——editorConfig](https://www.cnblogs.com/xiaohuochai/p/7160067.html)
