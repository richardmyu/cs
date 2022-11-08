# SQL 高级处理

[TOC]

## 1.窗口函数

### 1.1.什么是窗口函数

窗口函数也称为 `OLAP` 函数。**OLAP** 是 OnLine Analytical Processing 的简称，意思是【对数据库数据进行实时分析处理】。窗口函数就是为了实现 OLAP 而添加的标准 SQL 功能。

> MySQL  从 8.0 开始支持开窗函数，这个功能在大多商业数据库中早已支持，也叫 **分析函数**。

### 1.2.窗口函数的语法

```sql
-- []中的内容可以省略。
<窗口函数> OVER ([PARTITION BY <列清单>]
                         ORDER BY <排序用列清单>)
```

其中重要的关键字是 `PARTITION BY` 和 `ORDER BY`，理解这两个关键字的作用是理解窗口函数的关键。窗口函数大体可以分为以下两种：

1. 能够作为窗口函数的聚合函数（`SUM`、`AVG`、`COUNT`、`MAX`、`MIN`）；

2. `RANK`、`DENSE_RANK`、`ROW_NUMBER` 等 OLAP 专用函数；

聚合函数根据使用语法的不同，可以在聚合函数和窗口函数之间进行转换。

### 1.3.语法的基本使用方法 —— 使用 `RANK` 函数

正如其名称所示，`RANK` 是用来计算记录排序的函数。

```sql
SELECT
  product_name,
  product_type,
  sale_price,
  RANK () OVER (
    PARTITION BY product_type
    ORDER BY
      sale_price
  ) AS ranking
FROM
  Product;
/*
+--------------+--------------+------------+---------+
| product_name | product_type | sale_price | ranking |
+--------------+--------------+------------+---------+
| 圆珠笔       | 办公用品     |        100 |       1 |
| 打孔器       | 办公用品     |        500 |       2 |
| 叉子         | 厨房用具     |        500 |       1 |
| 擦菜板       | 厨房用具     |        880 |       2 |
| 菜刀         | 厨房用具     |       3000 |       3 |
| 高压锅       | 厨房用具     |       6800 |       4 |
| T恤衫        | 衣服         |       1000 |       1 |
| 运动T恤      | 衣服         |       4000 |       2 |
+--------------+--------------+------------+---------+
*/
```

`PARTITION BY` 能够设定排序的对象范围。`ORDER BY` 能够指定按照哪一列、何种顺序进行排序。

`ORDER BY` 与 `SELECT` 语句末尾的 `ORDER BY` 一样，可以通过关键字 `ASC/DESC` 来指定升序和降序。省略该关键字时会默认按照 `ASC`，也就是升序进行排序。

窗口函数兼具 `GROUP BY` 子句的分组功能以及 `ORDER BY` 子句的排序功能。但是，`PARTITION BY` 子句并不具备 `GROUP BY` 子句的汇总功能。因此，使用 `RANK` 函数并不会减少原表中记录的行数。

> **重点**：窗口函数兼具【分组】和【排序】两种功能，并不具备汇总功能。
> `GROUP BY` 子句有汇总功能（汇总意味着，数据会缩减为一条呈现），`PARTITION BY` 子句并没有。

通过 `PARTITION BY` 【分组】后的记录集合称为 **窗口**。此处的窗口并非“窗户”的意思，而是代表范围。这也是“窗口函数”名称的由来。

> 从词语意思的角度考虑，可能“组”比“窗口”更合适一些，但是在 SQL 中，“组”更多的是用来特指使用 `GROUP BY` 分割后的记录集合，因此，为了避免混淆，使用 `PARTITION BY` 时称为窗口。

此外，各个窗口在定义上绝对不会包含共通的部分。这与通过 `GROUP BY` 子句分割后的集合具有相同的特征。

### 1.4.无需指定 `PARTITION BY`

使用窗口函数时起到关键作用的是 `PARTITION BY` 和 `GROUP BY`。其中，`PARTITION BY` 并不是必需的，这和使用没有 `GROUP BY` 的聚合函数时的效果一样，也就是将整个表作为一个大的窗口来使用。

```sql
SELECT
  product_name,
  product_type,
  sale_price,
  RANK () OVER (
    ORDER BY
      sale_price
  ) AS ranking
FROM
  Product;
/*
+--------------+--------------+------------+---------+
| product_name | product_type | sale_price | ranking |
+--------------+--------------+------------+---------+
| 圆珠笔       | 办公用品     |        100 |       1 |
| 打孔器       | 办公用品     |        500 |       2 |
| 叉子         | 厨房用具     |        500 |       2 |
| 擦菜板       | 厨房用具     |        880 |       4 |
| T恤衫        | 衣服         |       1000 |       5 |
| 菜刀         | 厨房用具     |       3000 |       6 |
| 运动T恤      | 衣服         |       4000 |       7 |
| 高压锅       | 厨房用具     |       6800 |       8 |
+--------------+--------------+------------+---------+
*/
```

当希望先将表中的数据分为多个部分（窗口），再使用窗口函数时，可以使用 `PARTITION BY` 选项。

### 1.5.专用窗口函数的种类

1. **RANK 函数**

- 计算排序时，如果存在相同位次的记录，则会跳过之后的位次。

2. **DENSE_RANK 函数**

- 同样是计算排序，即使存在相同位次的记录，也不会跳过之后的位次。

3. **ROW_NUMBER 函数**

- 赋予唯一的连续位次。

```sql
SELECT
  product_name,
  product_type,
  sale_price,
  RANK () OVER (
    ORDER BY
      sale_price
  ) AS ranking,
  DENSE_RANK () OVER (
    ORDER BY
      sale_price
  ) AS dense_ranking,
  ROW_NUMBER () OVER (
    ORDER BY
      sale_price
  ) AS row_num
FROM
  Product;
/*
+--------------+--------------+------------+---------+---------------+---------+
| product_name | product_type | sale_price | ranking | dense_ranking | row_num |
+--------------+--------------+------------+---------+---------------+---------+
| 圆珠笔       | 办公用品     |        100 |       1 |             1 |       1 |
| 打孔器       | 办公用品     |        500 |       2 |             2 |       2 |
| 叉子         | 厨房用具     |        500 |       2 |             2 |       3 |
| 擦菜板       | 厨房用具     |        880 |       4 |             3 |       4 |
| T恤衫        | 衣服         |       1000 |       5 |             4 |       5 |
| 菜刀         | 厨房用具     |       3000 |       6 |             5 |       6 |
| 运动T恤      | 衣服         |       4000 |       7 |             6 |       7 |
| 高压锅       | 厨房用具     |       6800 |       8 |             7 |       8 |
+--------------+--------------+------------+---------+---------------+---------+
*/
```

由于专用窗口函数无需参数，因此通常括号中都是空的。这也是专用窗口函数通常的使用方式，这一点与作为窗口函数使用的聚合函数有很大的不同。

### 1.6.窗口函数的适用范围

函数大部分都没有使用位置的限制，最多也就是在 `WHERE` 子句中使用聚合函数时会有些注意事项。但是，使用窗口函数的位置却有非常大的限制。更确切地说，窗口函数只能书写在一个特定的位置。

这个位置就是 `SELECT` 子句之中。反过来说，就是这类函数不能在 `WHERE` 子句或者 `GROUP BY` 子句中使用。

> 语法上，除了 `SELECT` 子句，`ORDER BY` 子句或者 `UPDATE` 语句的 `SET` 子句中也可以使用。但因为几乎没有实际的业务示例，所以开始的时候只要记得“只能在 `SELECT` 子句中使用”就可以了。

但是为什么窗口函数只能在 `SELECT` 子句中使用呢？其理由就是，在 DBMS 内部，【窗口函数是对 `WHERE` 子句或者 `GROUP BY` 子句处理后的“结果”进行的操作】。在得到用户想要的结果之前，即使进行了排序处理，结果也是错误的。在得到排序结果之后，如果通过 `WHERE` 子句中的条件除去了某些记录，或者使用 `GROUP BY` 子句进行了汇总处理，那好不容易得到的排序结果也无法使用了。

正是由于这样的原因，在 `SELECT` 子句之外“使用窗口函数是没有意义的”，所以在语法上才会有这样的限制。

### 1.7.作为窗口函数使用的聚合函数

所有的聚合函数都能用作窗口函数，其语法和专用窗口函数完全相同，但需要在括号内指定作为汇总对象的列。

```sql
SELECT
  product_id,
  product_name,
  sale_price,
  SUM(sale_price) OVER (
    ORDER BY
      product_id
  ) AS current_sum
FROM
  Product;
/*
+------------+--------------+------------+-------------+
| product_id | product_name | sale_price | current_sum |
+------------+--------------+------------+-------------+
| 0001       | T恤衫        |       1000 |        1000 |
| 0002       | 打孔器       |        500 |        1500 |
| 0003       | 运动T恤      |       4000 |        5500 |
| 0004       | 菜刀         |       3000 |        8500 |
| 0005       | 高压锅       |       6800 |       15300 |
| 0006       | 叉子         |        500 |       15800 |
| 0007       | 擦菜板       |        880 |       16680 |
| 0008       | 圆珠笔       |        100 |       16780 |
+------------+--------------+------------+-------------+
*/
```

> **注意**：在 MySQL  中，使用聚合函数作为窗口函数时，不仅要指定参数，而且聚合函数和参数之间不能有空格，即 `SUM (sale_price)` 会报语法错误，正确的是：`SUM(sale_price)`。而在 PostgreSQL 中，两种都可以使用。

在按照时间序列的顺序，计算各个时间的销售额总额等的时候，通常都会使用这种称为 **累计** 的统计方法。

```sql
SELECT
  product_id,
  product_name,
  sale_price,
  AVG(sale_price) OVER (
    ORDER BY
      product_id
  ) AS current_avg
FROM
  Product;
/*
+------------+--------------+------------+-------------+
| product_id | product_name | sale_price | current_avg |
+------------+--------------+------------+-------------+
| 0001       | T恤衫        |       1000 |   1000.0000 |
| 0002       | 打孔器       |        500 |    750.0000 |
| 0003       | 运动T恤      |       4000 |   1833.3333 |
| 0004       | 菜刀         |       3000 |   2125.0000 |
| 0005       | 高压锅       |       6800 |   3060.0000 |
| 0006       | 叉子         |        500 |   2633.3333 |
| 0007       | 擦菜板       |        880 |   2382.8571 |
| 0008       | 圆珠笔       |        100 |   2097.5000 |
+------------+--------------+------------+-------------+
*/
```

以“自身记录（当前记录）”作为基准进行统计，就是将聚合函数当作窗口函数使用时的最大特征。

### 1.8.计算移动平均

窗口函数就是将表以窗口为单位进行分割，并在其中进行排序的函数。其实其中还包含在窗口中指定更加详细的汇总范围的备选功能，该备选功能中的汇总范围称为 **框架**。

```sql
SELECT
  product_id,
  product_name,
  sale_price,
  -- 需要在 ORDER BY 子句之后使用指定范围的关键字
  AVG(sale_price) OVER (
    ORDER BY
      product_id ROWS 2 PRECEDING
  ) AS moving_avg
FROM
  Product;
/*
+------------+--------------+------------+------------+
| product_id | product_name | sale_price | moving_avg |
+------------+--------------+------------+------------+
| 0001       | T恤衫        |       1000 |  1000.0000 |
| 0002       | 打孔器       |        500 |   750.0000 |
| 0003       | 运动T恤      |       4000 |  1833.3333 |
| 0004       | 菜刀         |       3000 |  2500.0000 |
| 0005       | 高压锅       |       6800 |  4600.0000 |
| 0006       | 叉子         |        500 |  3433.3333 |
| 0007       | 擦菜板       |        880 |  2726.6667 |
| 0008       | 圆珠笔       |        100 |   493.3333 |
+------------+--------------+------------+------------+
*/
```

这里使用了 `ROWS`（“行”）和 `PRECEDING`（“之前”）两个关键字，将框架指定为 “截止到之前 `~` 行”，因此 “`ROWS 2 PRECEDING`” 就是将框架指定为 “截止到之前 2 行”，也就是将作为汇总对象的记录限定为如下的“最靠近的 3 行”。

- 自身（当前记录）
- 之前 1 行的记录
- 之前 2 行的记录

也就是说，由于框架是根据当前记录来确定的，因此和固定的窗口不同，其范围会随着当前记录的变化而变化。

如果将条件中的数字变为“ROWS 5 PRECEDING”，就是“截止到之前 5 行”（最靠近的 6 行）的意思。这样的统计方法称为 **移动平均**（moving average）。由于这种方法在希望实时把握“最近状态”时非常方便，因此常常会应用在对股市趋势的实时跟踪当中。

使用关键字 `FOLLOWING`（“之后”）替换 `PRECEDING`，就可以指定“截止到之后`~` 行”作为框架了。如果希望将当前记录的前后行作为汇总对象时，同时使用 `PRECEDING`（“之前”）和 `FOLLOWING`（“之后”）关键字来实现。

```sql
SELECT
  product_id,
  product_name,
  sale_price,
  AVG (sale_price) OVER (
    ORDER BY
      product_id ROWS BETWEEN 1 PRECEDING
      AND 1 FOLLOWING
  ) AS moving_avg
FROM
  Product;
/*
+------------+--------------+------------+------------+
| product_id | product_name | sale_price | moving_avg |
+------------+--------------+------------+------------+
| 0001       | T恤衫        |       1000 |   750.0000 |
| 0002       | 打孔器       |        500 |  1833.3333 |
| 0003       | 运动T恤      |       4000 |  2500.0000 |
| 0004       | 菜刀         |       3000 |  4600.0000 |
| 0005       | 高压锅       |       6800 |  3433.3333 |
| 0006       | 叉子         |        500 |  2726.6667 |
| 0007       | 擦菜板       |        880 |   493.3333 |
| 0008       | 圆珠笔       |        100 |   490.0000 |
+------------+--------------+------------+------------+
*/
```

### 1.9.两个 `ORDER BY`

使用窗口函数时与结果形式相关的一个注意事项，那就是记录的排列顺序。`OVER` 子句中的 `ORDER BY` 只是用来决定窗口函数按照什么样的顺序进行计算的，对结果的排列顺序并没有影响。

```sql
SELECT
  product_id,
  product_name,
  sale_price,
  RANK() OVER (
    ORDER BY
      sale_price
  ) AS ranking
FROM
  Product;
/*
+------------+--------------+------------+---------+
| product_id | product_name | sale_price | ranking |
+------------+--------------+------------+---------+
| 0008       | 圆珠笔       |        100 |       1 |
| 0002       | 打孔器       |        500 |       2 |
| 0006       | 叉子         |        500 |       2 |
| 0007       | 擦菜板       |        880 |       4 |
| 0001       | T恤衫        |       1000 |       5 |
| 0004       | 菜刀         |       3000 |       6 |
| 0003       | 运动T恤      |       4000 |       7 |
| 0005       | 高压锅       |       6800 |       8 |
+------------+--------------+------------+---------+
*/

SELECT
  product_id,
  product_name,
  sale_price,
  RANK() OVER (
    ORDER BY
      sale_price
  ) AS ranking
FROM
  Product -- 对结果排序
ORDER BY
  ranking;
/*
+------------+--------------+------------+---------+
| product_id | product_name | sale_price | ranking |
+------------+--------------+------------+---------+
| 0008       | 圆珠笔       |        100 |       1 |
| 0002       | 打孔器       |        500 |       2 |
| 0006       | 叉子         |        500 |       2 |
| 0007       | 擦菜板       |        880 |       4 |
| 0001       | T恤衫        |       1000 |       5 |
| 0004       | 菜刀         |       3000 |       6 |
| 0003       | 运动T恤      |       4000 |       7 |
| 0005       | 高压锅       |       6800 |       8 |
+------------+--------------+------------+---------+
*/
```

有些 DBMS 也可以按照窗口函数的 `ORDER BY` 子句所指定的顺序对结果进行排序，但那也仅仅是个例而已。

那就是在 `SELECT` 语句的最后，使用 `ORDER BY` 子句进行指定。这样就能保证 `SELECT` 语句的结果中记录的排列顺序了，除此之外也没有其他办法了。

> 将聚合函数作为窗口函数使用时，会以当前记录为基准来决定汇总对象的记录。

## 2.`GROUPING` 运算符

PostgreSQL 支持，但 MySQL  不支持 `GROUPING` 运算符，目前仅仅支持 `ROLLUP`。

### 2.0.同时计算出合计值

```sql
SELECT product_type, SUM(sale_price)
  FROM Product
GROUP BY product_type;
/*
+--------------+-----------------+
| product_type | SUM(sale_price) |
+--------------+-----------------+
| 衣服         |            5000 |
| 办公用品     |             600 |
| 厨房用具     |           11180 |
+--------------+-----------------+
*/
```

`GROUP BY` 子句是用来指定聚合键的场所，所以只会根据这里指定的键分割数据，当然不会出现合计行。而合计行是不指定聚合键时得到的汇总结果，因此与下面的 3 行通过聚合键得到的结果并不相同。按照通常的思路，想一次得到这两种结果是不可能的。

如果想要获得那样的结果，通常的做法是分别计算出合计行和按照商品种类进行汇总的结果，然后通过 `UNION ALL` 连接在一起。

> 虽然也可以使用 `UNION` 来代替 `UNION ALL`，但由于两条 `SELECT` 语句的聚合键不同，一定不会出现重复行，因此可以使用 `UNION ALL`。`UNION ALL` 和 `UNION` 的不同之处在于它不会对结果进行排序，因此比 `UNION` 的性能更好。

```sql
SELECT "合计" AS product_type, SUM(sale_price)
  FROM Product
UNION ALL
SELECT product_type, SUM(sale_price)
  FROM Product
GROUP BY product_type;
/*
+--------------+-----------------+
| product_type | SUM(sale_price) |
+--------------+-----------------+
| 合计         |           16780 |
| 衣服         |            5000 |
| 办公用品     |             600 |
| 厨房用具     |           11180 |
+--------------+-----------------+
*/
```

为了满足用户的需求，标准 SQL 引入了 `GROUPING` 运算符，使用该运算符就能通过非常简单的 SQL 得到汇总单位不同的汇总结果了。

`GROUPING` 运算符包含以下 3 种：

- `ROLLUP`
- `CUBE`
- `GROUPING SETS`

### 2.1.`ROLLUP` -- 同时得出合计和小计

```sql
-- PostgreSQL
SELECT
  product_type,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  ROLLUP(product_type);

-- MySQL
SELECT
  product_type,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  product_type WITH ROLLUP;
/*
 product_type | sum_price
--------------+-----------
              |     16780
 衣服         |      5000
 办公用品     |       600
 厨房用具     |     11180
*/
```

从语法上来说，就是将 `GROUP BY` 子句中的聚合键清单像 `ROLLUP(< 列 1>,< 列 2>,...)` 这样使用。该运算符的作用，一言以蔽之，就是“一次计算出不同聚合键组合的结果”。

在本例中就是一次计算出了如下两种组合的汇总结果。

1. `GROUP BY ()`
2. `GROUP BY (product_type)`

`GROUP BY ()` 表示没有聚合键，也就相当于没有 `GROUP BY` 子句（这时会得到全部数据的合计行的记录），该合计行记录称为 **超级分组记录**（super group row）。超级分组记录的 `product_type` 列的键值（对 DBMS 来说）并不明确，因此会默认使用 `NULL`。

```SQL
SELECT
  product_type,
  regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  product_type,
  regist_date;
/*
+--------------+-------------+-----------+
| product_type | regist_date | sum_price |
+--------------+-------------+-----------+
| 衣服         | 2009-09-20  |      1000 |
| 办公用品     | 2009-09-11  |       500 |
| 衣服         | NULL        |      4000 |
| 厨房用具     | 2009-09-20  |      3500 |
| 厨房用具     | 2009-01-15  |      6800 |
| 厨房用具     | 2008-04-28  |       880 |
| 办公用品     | 2009-11-11  |       100 |
+--------------+-------------+-----------+
*/

-- PostgreSQL
SELECT
  product_type,
  regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  ROLLUP(product_type, regist_date);

-- MySQL
SELECT
  product_type,
  regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  product_type,
  regist_date WITH ROLLUP;
/*
+--------------+-------------+-----------+
| product_type | regist_date | sum_price |
+--------------+-------------+-----------+
| 办公用品     | 2009-09-11  |       500 |
| 办公用品     | 2009-11-11  |       100 |
| 办公用品     | NULL        |       600 |
| 厨房用具     | 2008-04-28  |       880 |
| 厨房用具     | 2009-01-15  |      6800 |
| 厨房用具     | 2009-09-20  |      3500 |
| 厨房用具     | NULL        |     11180 |
| 衣服         | NULL        |      4000 |
| 衣服         | 2009-09-20  |      1000 |
| 衣服         | NULL        |      5000 |
| NULL         | NULL        |     16780 |
+--------------+-------------+-----------+
*/
```

等效汇总结果：

1. `GROUP BY ()`
2. `GROUP BY (product_type)`
3. `GROUP BY (product_type, regist_date)`

`ROLLUP` 是“卷起”的意思，比如卷起百叶窗、窗帘卷，等等。其名称也形象地说明了该操作能够得到像从小计到合计这样，从最小的聚合级开始，聚合单位逐渐扩大的结果。

### 2.2.`GROUPING` -- 让 `NULL` 更加容易分辨

`ROLLUP` 无法区分本身没有数据 `NULL` 和超级分组记录导致的 `NULL` 两种情况，为了避免混淆，SQL 提供了一个用来判断超级分组记录的 `NULL` 的特定函数 —— `GROUPING` 函数。该函数在其参数列的值为超级分组记录所产生的 `NULL` 时返回 1，其他情况返回 0。

```sql
-- PostgreSQL
SELECT
  GROUPING(product_type) AS product_type,
  GROUPING(regist_date) AS regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  ROLLUP(product_type, regist_date);

-- MySQL
SELECT
  GROUPING(product_type) AS product_type,
  GROUPING(regist_date) AS regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  product_type, regist_date WITH ROLLUP;
/*
+--------------+-------------+-----------+
| product_type | regist_date | sum_price |
+--------------+-------------+-----------+
|            0 |           0 |       500 |
|            0 |           0 |       100 |
|            0 |           1 |       600 |
|            0 |           0 |       880 |
|            0 |           0 |      6800 |
|            0 |           0 |      3500 |
|            0 |           1 |     11180 |
|            0 |           0 |      4000 |
|            0 |           0 |      1000 |
|            0 |           1 |      5000 |
|            1 |           1 |     16780 |
+--------------+-------------+-----------+
*/

-- 插入恰当的字符串
-- PostgreSQL
SELECT
  CASE
    WHEN GROUPING(product_type) = 1 THEN '商品种类 合计'
    ELSE product_type
  END AS product_type,
  CASE
    WHEN GROUPING(regist_date) = 1 THEN '登记日期 合计' -- 满足 CASE 表达式所有分支的返回值必须一致的条件
    ELSE CAST(regist_date AS VARCHAR(16))
  END AS regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  ROLLUP(product_type, regist_date);
/*
 product_type  |  regist_date  | sum_price
---------------+---------------+-----------
 商品种类 合计 | 登记日期 合计 |     16780
 衣服          |               |      4000
 厨房用具      | 2008-04-28    |       880
 衣服          | 2009-09-20    |      1000
 办公用品      | 2009-11-11    |       100
 厨房用具      | 2009-01-15    |      6800
 办公用品      | 2009-09-11    |       500
 厨房用具      | 2009-09-20    |      3500
 衣服          | 登记日期 合计 |      5000
 办公用品      | 登记日期 合计 |       600
 厨房用具      | 登记日期 合计 |     11180
*/

-- MySQL
SELECT
  CASE
    WHEN GROUPING(product_type) = 1 THEN '商品种类 合计'
    ELSE product_type
  END AS product_type,
  CASE
    WHEN GROUPING(regist_date) = 1 THEN '登记日期 合计'
    ELSE CAST(regist_date AS CHAR(16))
  END AS regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  product_type,
  regist_date WITH ROLLUP;
/*
+---------------+---------------+-----------+
| product_type  | regist_date   | sum_price |
+---------------+---------------+-----------+
| 办公用品      | 2009-09-11    |       500 |
| 办公用品      | 2009-11-11    |       100 |
| 办公用品      | 登记日期 合计 |       600 |
| 厨房用具      | 2008-04-28    |       880 |
| 厨房用具      | 2009-01-15    |      6800 |
| 厨房用具      | 2009-09-20    |      3500 |
| 厨房用具      | 登记日期 合计 |     11180 |
| 衣服          | NULL          |      4000 |
| 衣服          | 2009-09-20    |      1000 |
| 衣服          | 登记日期 合计 |      5000 |
| 商品种类 合计 | 登记日期 合计 |     16780 |
+---------------+---------------+-----------+
*/
```

要将 `SELECT` 子句中的 `regist_date` 列转换为 `CAST(regist_date AS VARCHAR)16))` 形式的字符串,这是为了满足 `CASE` 表达式所有分支的返回值必须一致的条件。如果不这样的话，那么各个分支会分别返回日期类型和字符串类型的值，执行时就会发生语法错误。

### 2.3.`CUBE` -- 用数据来搭积木

`CUBE` 的语法和 `ROLLUP` 相同，只需要将 `ROLLUP` 替换为 `CUBE` 就可以了。

```sql
-- PostgreSQL
SELECT
  CASE
    WHEN GROUPING(product_type) = 1 THEN '商品种类 合计'
    ELSE product_type
  END AS product_type,
  CASE
    WHEN GROUPING(regist_date) = 1 THEN '登记日期 合计'
    ELSE CAST(regist_date AS VARCHAR(16))
  END AS regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  CUBE(product_type, regist_date);
/*
 product_type  |  regist_date  | sum_price
---------------+---------------+-----------
 商品种类 合计 | 登记日期 合计 |     16780
 衣服          |               |      4000
 厨房用具      | 2008-04-28    |       880
 衣服          | 2009-09-20    |      1000
 办公用品      | 2009-11-11    |       100
 厨房用具      | 2009-01-15    |      6800
 办公用品      | 2009-09-11    |       500
 厨房用具      | 2009-09-20    |      3500
 衣服          | 登记日期 合计 |      5000
 办公用品      | 登记日期 合计 |       600
 厨房用具      | 登记日期 合计 |     11180
 商品种类 合计 |               |      4000
 商品种类 合计 | 2009-11-11    |       100
 商品种类 合计 | 2009-09-20    |      4500
 商品种类 合计 | 2009-09-11    |       500
 商品种类 合计 | 2009-01-15    |      6800
 商品种类 合计 | 2008-04-28    |       880
*/
```

所谓 `CUBE`，就是将 `GROUP BY` 子句中聚合键的“所有可能的组合”的汇总结果集中到一个结果中。因此，组合的个数就是 2n（n 是聚合键的个数）。

1. `GROUP BY ()`
2. `GROUP BY (product_type)`
3. `GROUP BY (regist_date)` ←添加的组合
4. `GROUP BY (product_type, regist_date)`

> 使用 `ROLLUP` 时组合的个数是 n + 1。随着组合个数的增加，结果的行数也会增加，因此如果使用 `CUBE` 时不加以注意的话，往往会得到意想不到的巨大结果。顺带说一下，`ROLLUP` 的结果一定包含在 `CUBE` 的结果之中。

### 2.4.`GROUPING SETS` -- 取得期望的积木

与 `ROLLUP` 或者 `CUBE` 能够得到规定的结果相对，`GROUPING SETS` 用于从中取出个别条件对应的不固定的结果。然而，由于期望获得不固定结果的情况少之又少，因此与 `ROLLUP` 或者 `CUBE` 比起来，使用 `GROUPING SETS` 的机会也就很少了。

```sql
-- PostgreSQL
SELECT
  CASE
    WHEN GROUPING(product_type) = 1 THEN '商品种类 合计'
    ELSE product_type
  END AS product_type,
  CASE
    WHEN GROUPING(regist_date) = 1 THEN '登记日期 合计'
    ELSE CAST(regist_date AS CHAR(16))
  END AS regist_date,
  SUM(sale_price) AS sum_price
FROM
  Product
GROUP BY
  GROUPING SETS (product_type, regist_date);
/*
 product_type  |  regist_date  | sum_price
---------------+---------------+-----------
 衣服          | 登记日期 合计 |      5000
 办公用品      | 登记日期 合计 |       600
 厨房用具      | 登记日期 合计 |     11180
 商品种类 合计 |               |      4000
 商品种类 合计 | 2009-11-11    |       100
 商品种类 合计 | 2009-09-20    |      4500
 商品种类 合计 | 2009-09-11    |       500
 商品种类 合计 | 2009-01-15    |      6800
 商品种类 合计 | 2008-04-28    |       880
*/
```
