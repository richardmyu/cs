# SQL

> 基本以 PostgreSQL 和 mySQL 语法为主。

## 2.基础查询

### 2.1.`SELECT` 语句基础

1. 使用 `SELECT` 语句从表中选取数据。
>
2. 为列设定显示用的别名。
>
3. `SELECT` 语句中可以使用常数或者表达式。
>
4. 通过指定 `DISTINCT` 可以删除重复的行。
>
5. SQL 语句中可以使用注释。
>
6. 可以通过 `WHERE` 语句从表中选取出符合查询条件的数据。

### 2.2.算术运算符和比较运算符

1. 运算符就是对其两边的列或者值进行运算（计算或者比较大小等）的符号。
>
2. 使用算术运算符可以进行四则运算。
>
3. 括号可以提升运算的优先顺序（优先进行运算）。
>
4. 包含 `NULL` 的运算，其结果也是 `NULL`。
>
5. 比较运算符可以用来判断列或者值是否相等，还可以用来比较大小。
>
6. 判断是否为 `NULL`，需要使用 `IS NULL` 或者 `IS NOT NULL` 运算符。

### 2.3.逻辑运算符

1. 通过使用逻辑运算符，可以将多个查询条件进行组合。
>
2. 通过 `NOT` 运算符可以生成“不是~”这样的查询条件。
>
3. 两边条件都成立时，使用 `AND` 运算符的查询条件才成立。
>
4. 只要两边的条件中有一个成立，使用 `OR` 运算符的查询条件就可以成立。
>
5. 值可以归结为真（`TRUE`）和假（`FALSE`）其中之一的值称为真值。比较运算符在比较成立时返回真，不成立时返回假。但是，在 SQL 中还存在另外一个特定的真值——不确定（`UNKNOWN`）。
>
6. 将根据逻辑运算符对真值进行的操作及其结果汇总成的表称为真值表。
>
7. SQL 中的逻辑运算是包含对真、假和不确定进行运算的三值逻辑。

---

必读

- [x] 1.《SQL基础教程》(第二版) MICK --（PostgreSQL 向）
- [ ] 2.《MySQL必知必会》Ben Forta
- [ ] 3.[SQL 教程](https://www.runoob.com/sql/sql-tutorial.html) --（MySQL 向）
- [ ] 4.[sqlbolt](https://sqlbolt.com/)

参考：

1.[PostgreSQL 教程](https://www.runoob.com/postgresql/postgresql-tutorial.html)
2.[PostgreSQL 13.1 手册](http://www.postgres.cn/docs/13/index.html)
3.[PostgreSQL(数据库)资料](https://github.com/ty4z2008/Qix/blob/master/pg.md)
