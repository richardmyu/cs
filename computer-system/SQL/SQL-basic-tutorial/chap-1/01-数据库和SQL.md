# 数据库和 SQL

[TOC]

## 1.数据库是什么

**数据库** (Database, **DB**) 是将大量数据保存起来，通过计算机加工而成的可以进行高效访问的数据集合。用来管理数据库的计算机系统称为 **数据库管理系统** (Database Management System, **DBMS**)。

### 1.1.DBMS 的种类

DBMS 主要通过数据的保存格式（数据库的种类）来进行分类。主要有：

1. **层次数据库**（Hierarchical Database, **HDB**）

- 把数据通过层次结构（树形结构）的方式表现出来。

2. **关系数据库**（Relational Database, **RDB**）

- 采用由行和列组成的二维表来管理数据，同时，使用 SQL（Structured Query Language，结构化查询语言）对数据进行操作。
- 代表性的 RDBMS:
  - Oracle Database: 甲骨文
  - SQL Server: 微软
  - DB2: IBM
  - PostgreSQL: 开源
  - MySQL: 开源

3. **面向对象数据库**（Object Oriented Database, **OODB**）

- 把数据以及对数据的操作集合起来以对象位单位进行管理。

4. **XML 数据库**（XML Database, **XMLDB**）

- XML 数据库可以对 XML 形式的大量数据进行高速处理。

5. **键值存储系统**（Key-Value Store, **KVS**）

- 单纯用来保存查询所使用的主键（Key）和值（Value）的组合的数据库。

## 2.数据库的结构

### 2.1.RDNMS 的常见系统结构

最常见的系统结构就是 **客户端/服务器类型（C/S 类型）**。

```markdown
------------------                   -------------------
                  ----  SQL 语句 --->      服务器
      客户端                               RDBMS
（使用数据库的程序                      （读取数据库的程序）
                  <--- 请求的数据 ----
------------------                   -------------------
                                           ▲▲
                                           ||
                                           ▼▼
                                      --------------------
                                          数据库
                                      把数据保存到硬盘等设备上
                                      --------------------
```

**服务器** 指的是用来接收其他程序发出的请求，并对该请求进行相应处理的程序（软件），或者是安装了此类程序的设备（计算机）。

向服务器发出请求的程序（软件），或者是安装了该程序的设备（计算机）称为 **客户端**。

### 2.2.表的结构

用来管理数据的二维表在关系数据库中简称为 **表**。根据 SQL 语句的内容返回的数据同样必须是二维表的形式，这也是关系数据库的特征之一。返回结果如果不是二维表的 SQL 语句则无法执行。

表的列（垂直方向）称为 **字段**，它代表了保存在表中的数据项目。与之相对，表的行（水平方向）称为 **记录**，它相当于一条数据。

> *关系数据库必须以行为单位进行数据读写*。

行和列交汇的方格可以简单称为 **单元格**，一个单元格中只能输入一个数据。

## 3.SQL 概要

SQL 就是访问和处理关系数据库的计算机标准语言。SQL 用关键字、表名、列名等组合而成的一条语句（SQL 语句）来描述操作的内容。根据对 RDBMS 赋予的指令种类的不同，SQL 语句可以分为以下三类。

1. **DDL**（Data Definition Language, **数据定义语言**）

- 用来创建或者删除存储数据用的数据库以及数据库中的表等对象。DDL 包含以下几种指令：
  - `CREATE`：创建数据库和表等对象
  - `DROP`：删除数据库和表等对象
  - `ALTER`：修改数据库和表等对象的结构

2. **DML**（Data Manipulation Language, **数据操纵语言**）

- 用来查询或者变更表中的记录。DML 包含以下几种指令：
  - `SELECT`：查询表中的数据
  - `INSERT`：向表中插入新数据
  - `UPDATE`：更新表中的数据
  - `DELETE`：删除表中的数据

3. **DCL**（Data Control Language, **数据控制语言**）

- 用来确认或者取消对数据库中的数据进行的变更。除此之外，还可以对 RDBMS 的用户是否有权限操作数据库中的对象（数据库表等）进行设定。DCL 包含以下几种指令：
  - `COMMIT`：确认对数据库中的数据进行变更
  - `ROLLBACK`：取消对数据库中的数据进行变更
  - `GRANT`：赋予用户操作权限
  - `REVOKE`：取消用户的操作权限

> 实际使用的 SQL 语句当中有 90% 属于 DML。

### 3.1.SQL 书写基本规则

1. SQL 语句要以分号（`;`）结尾；
2. SQL 语句不区分大小写；（但插入到表中的数据是区分大小写的）
3. 常数的书写方式是固定的：

- 字符串：用单引号（`''`）标识；
- 日期：也用单引号标识；
- 数字：无需标识；
- 特别的，中文需要双引号（`""`）标识；

4. 单词（关键字）需要用半角空格或换行来分隔（使用全角空格做分隔符，会发生错误，无法预期结果）；

## 4.表的创建

- **创建数据库**

```sql
CREATE DATABASE <数据库名称>;
```

- **创建表**

```sql
CREATE TABLE <表名>
(<列名 1><数据类型><该列所需约束>,
<列名 2><数据类型><该列所需约束>,
<列名 3><数据类型><该列所需约束>,
<列名 4><数据类型><该列所需约束>,
    ...
<该表的约束 1>, <该表的约束 2>, ...);
```

### 4.1.命名规范

1. 只能使用半角英文字母、数字、下划线（`_`）作为数据库、表和列的名称。

2. 名称必须以半角英文字母开头。

3. 在同一个数据库中不能创建两个相同名称的表，在同一个表中也不能创建两个名称相同的列。

### 4.2.数据类型

> 所有的列都必须指定数据类型。

**数据类型** 表示数据的种类，包括数字型、字符型和日期型等。每一列都不能存储与该列数据类型不符的数据。

四种基本类型：

1. **INTEGER**

用来指定存储整数的列的数据类型（数字型），不能存储小数。

2. **CHAR**

`CHAR` 是 `CHARACTER`（字符）的缩写，是用来指定存储字符串的列的数据类型（字符型）。字符串以 *定长字符串* 的形式存储在被指定为 `CHAR` 型的列中。

> 所谓定长字符串，就是当列中存储的字符串长度达不到最大长度的时候，使用半角空格进行补足。像 `CHAR(10)` 或者 `CHAR(200)` 这样，在括号中指定该列可以存储的字符串的长度（最大长度）。

3. **VARCHAR**

同 `CHAR` 类型一样，`VARCHAR` 型也是用来指定存储字符串的列的数据类型（字符串类型），也可以通过括号内的数字来指定字符串的长度（最大长度）。

但该类型的列是以可变长字符串的形式来保存字符串的 12。定长字符串在字符数未达到最大长度时会用半角空格补足，但可变长字符串不同，即使字符数未达到最大长度，也不会用半角空格补足。

4. **DATE**

用来指定存储日期（年月日）的列的数据类型（日期型）。

### 4.3.约束的设置

**约束** 是除了数据类型之外，对列中存储的数据进行限制或者追加条件的功能。

- **NOT NULL 约束**

`NULL` 是代表空白（无记录）的关键字。在 `NULL` 之前加上了表示否定的 `NOT`，就是给该列设置了不能输入空白，也就是必须输入数据的约束（如果什么都不输入就会出错）。

- **主键约束**

所谓 **键**，就是在指定特定数据时使用的列的组合。键种类多样，**主键**（primary key）就是可以特定一行数据的列，也可以说是唯一确定一行数据。

## 5.表的删除和更新

- **删除表**

```sql
DROP TABLE <表名>;
```

> 需要特别注意的是，删除的表是无法恢复的（其实很多 RDBMS 都预留了恢复的功能）。即使是被误删的表，也无法恢复，只能重新创建，然后重新插入数据。

- **添加/更新列**

```sql
ALTER TABLE <表名> ADD COLUMN <列的定义>;
```

- **删除列**

```sql
ALTER TABLE <表名> DROP COLUMN <列名>;
```

> `ALTER TABLE` 语句和 `DROP TABLE` 语句一样，执行之后无法恢复。误添的列可以通过 `ALTER TABLE` 语句删除，或者将表全部删除之后重新再创建。

- **插入数据**

```sql
-- pg
BEGIN TRANSACTION;
-- mysql
START TRANSACTION;

-- mysql
-- START TRANSACTION;
INSERT INTO Product VALUES ('0001', 'T 恤衫', '衣服', 1000, 500, '2009-09-20');
INSERT INTO Product VALUES ('0002', '打孔器', '办公用品', 500, 320, '2009-09-11');
INSERT INTO Product VALUES ('0003', '运动 T 恤', '衣服', 4000, 2800, NULL);
INSERT INTO Product VALUES ('0004', '菜刀', '厨房用具', 3000, 2800, '2009-09-20');
INSERT INTO Product VALUES ('0005', '高压锅', '厨房用具', 6800, 5000, '2009-01-15');
INSERT INTO Product VALUES ('0006', '叉子', '厨房用具', 500, NULL, '2009-09-20');
INSERT INTO Product VALUES ('0007', '擦菜板', '厨房用具', 880, 790, '2008-04-28');
INSERT INTO Product VALUES ('0008', '圆珠笔', '办公用品', 100, NULL,'2009-11-11');

COMMIT;
```

开头的 `BEGIN TRANSACTION` 语句是开始插入行的指令语句，结尾的 `COMMIT` 语句是确定插入行的指令语句。

> 插入数据中，只能用单引号（查询的时候也是）；并且插入数据后，无法再添加列。

- **表名的修改**

```sql
-- pg
ALTER TABLE old_name RENAME TO new_name;

-- mysql
RENAME TABLE old_name TO new_name;
```

> 各个数据库的语法都不尽相同，是因为标准 SQL 并没有 `RENAME`。
