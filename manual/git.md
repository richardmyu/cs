# Git

## 1.`git commit` 提交信息动态绑定时间

```shell
git commit -m "`date`" # Wed Aug 28 10:22:06 CST 2022
git commit -m "`date +'%Y-%m-%d'`" # 2022-08-28
git commit -m "Updated: `date +'%Y-%m-%d %H:%M:%S'`" # Updated: 2022-08-28 10:22:06
```

## 2.`git commit` 提交信息模板

- feat：新功能（feature）
- fix：修补 bug
- docs：文档（documentation）
- style： 格式（不影响代码运行的变动）
- refactor：重构（即不是新增功能，也不是修改 bug 的代码变动）
- test：增加测试
- chore：构建过程或辅助工具的变动

文件处理：

- add 新增
- rm 删除
- mod 修改
