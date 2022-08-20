# gitignore

`gitignore` 文件中的每一行都指定了一个模式。在决定是否忽略路径时，Git 通常会检查来自多个来源的 `gitignore` 模式，按照优先级顺序，从高到低（在一个优先级内，最后匹配的模式决定结果）。

## 格式规范

- 空行不匹配任何文件，因此它可以用作可读性的分隔符。
- 以 `＃` 开头的行，是注释行，都会被 Git 忽略。
- 可以使用标准的 `glob` 模式匹配。
- 匹配模式可以以（`/`）开头防止递归：
  - 比如 `a.md`，会遍历所有目录，而 `/a.md` 只会在根目录查找；
  - 如果模式的开头或中间（或两者）有一个分隔符，则该模式是相对于特定 `.gitignore` 文件本身的目录级别的。 否则模式也可能在低于 `.gitignore` 级别的任何级别匹配。
  - 如果模式中已经有一个中间斜线，则前导斜线是不相关的。
- 匹配模式可以以（`/`）结尾指定（更确切的是说法，是**区分**）目录：
  - 目录和文件同名：如果模式末尾有分隔符，则模式将只匹配目录，否则模式可以匹配文件和目录。
- 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（`!`）取反。一个可选的前缀 `!`  **否定模式**；任何被先前模式排除的匹配文件将再次包含在内。如果排除了该文件的父目录，则无法重新包含该文件。出于性能原因，Git 不会列出排除的目录，因此包含文件的任何模式都不起作用，无论它们在哪里定义。

> git 对于 `.ignore` 配置文件是按行从上到下进行规则匹配的，意味着如果前面的规则匹配的范围更大，则后面的规则将不会生效。

**glob 模式匹配**

| characters | descirption                                    |
| ---------- | ---------------------------------------------- |
| `*`        | 匹配任何字符串，路径分隔符 (`/`) 除外          |
| `**`       | 匹配任何字符串（包括路径分隔符）               |
| `?`        | 匹配任何单字符，路径分隔符 (`/`) 除外          |
| `[a-zA-Z]` | 范围匹配，匹配 `a-z` 或 `A-Z` 中的任意单个字符 |

> 其他连续的星号被视为常规星号，将根据之前的规则进行匹配。

## 移除已跟踪文件/文件夹

```shell
git rm --cached filename

# 移除文件夹时，要添加 `-r` 参数
git rm -r --cahced foldername
```

## 跟踪被限制的文件

```shell
# .gitignore
# /test/
git add test
# The following paths are ignored by one of your .gitignore files:
# test
# Use -f if you really want to add them.

# `-f` 强制添加 (添加空目录/文件夹是无效的，且无意义的)
git add -f test

# 查看
git check-ignore -v test
# .gitignore:10:/test/      test
```

> [Git FAQ:Can I add empty directories?](https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F)
> Currently the design of the Git index (staging area) only permits files to be listed, and nobody competent enough to make the change to allow empty directories has cared enough about this situation to remedy it.
>
> Directories are added automatically when adding files inside them. That is, directories never have to be added to the repository, and are not tracked on their own.
>
> You can say "`git add <dir>`" and it will add the files in there.
>
> If you really need a directory to exist in checkouts you should create a file in it. `.gitignore` works well for this purpose (there is also a tool MarkEmptyDirs using the .NET framework which allows you to automate this task); you can leave it empty or fill in the names of files you do not expect to show up in the directory.

---

参考：

1.[git-gitignore](https://git-scm.com/docs/gitignore/en)

2.[github/gitignore](https://github.com/github/gitignore)

3.[忽略特殊文件](https://www.liaoxuefeng.com/wiki/896043488029600/900004590234208)

4.[Git 忽略提交规则 - .gitignore 配置运维总结](https://www.cnblogs.com/kevingrace/p/5690241.html)
