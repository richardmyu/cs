# 快捷命令

## 查看/创建/删除数据库

```sql
-- 查看
-- PostgreSQL - 1
\l

-- PostgreSQL - 2 更多信息
\l+
-- or
\list+

-- PostgreSQL - 3 仅显示数据库的名称
SELECT datname FROM pg_database;

SHOW DATABESES; -- MySQL


-- 查看当前
-- MySQL - 1
SELECT DATABASE();

-- MySQL - 2 查看输出第一行：Tables_in_xxx
SHOW TABLES;

-- MySQL - 3 查看：Curren database
STATUS;

SELECT CURRENT_DATABASE();  -- PostgreSQL


-- 创建
CREATE DATABASE dbname;


-- 使用/切换
\c dbname  -- PostgreSQL
use dbname;  -- MySQL


-- 删除
DROP DATABASE dbname;
```

## 查看/创建/删除表

```sql
-- 查看
\dt  -- PostgreSQL
\dt+  -- PostgreSQL 更多信息
SHOW TABLES;  -- MySQL
SHOW FULL TABLES;  -- MySQL

-- 创建
CREATE TABLE table_name (
  -- 非空约束
  column_name date_type [NOT NULL],
  column_name date_type,
  ...
  PRIMARY KEY (一列或多列)
  );

-- 删除
DROP TABLE table_name;
```
