# 快捷命令

## 查看/创建/删除数据库

```sql
/*****************
** 查看【数据库】 **
*****************/

\l  -- PostgreSQL - 1
\l+  -- PostgreSQL - 2 更多信息
\list+  -- or
SELECT datname FROM pg_database;  -- PostgreSQL - 3 仅显示数据库的名称

SHOW DATABESES; -- MySQL


/********************
** 查看当前【数据库】 **
*********************/
SELECT DATABASE();  -- MySQL - 1
STATUS;  -- MySQL - 2 查看：Curren database
SELECT CURRENT_DATABASE();  -- PostgreSQL

/*****************
** 创建【数据库】 **
*****************/
CREATE DATABASE dbname;

/*********************
** 使用/切换【数据库】 **
*********************/
\c dbname;  -- PostgreSQL
use dbname;  -- MySQL

/*****************
** 删除【数据库】 **
*****************/
DROP DATABASE dbname;
```

## 查看/创建/删除表

```sql
/**************
** 查看【表】 **
**************/
\dt  -- PostgreSQL
\dt+  -- PostgreSQL 更多信息

SHOW TABLES;  -- MySQL
SHOW FULL TABLES;  -- MySQL

/**************
** 创建【表】 **
**************/
CREATE TABLE table_name (
  -- 非空约束
  column_name date_type [NOT NULL],
  column_name date_type,
  ...
  PRIMARY KEY (一列或多列)
  );

/**************
** 删除【表】 **
**************/
DROP TABLE table_name;
```
