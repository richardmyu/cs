-- 题目 组合 Products 表中的产品名称和 Customers 表中的顾客名称
-- 关键字 组合查询
SELECT
  prod_name
FROM
  Products
UNION
SELECT
  cust_name
FROM
  Customers
ORDER BY
  prod_name;
