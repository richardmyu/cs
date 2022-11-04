-- 题目
-- 关键字 汇总数据
SELECT
  MAX(prod_price) AS max_price
FROM
  Products
WHERE
  prod_price <= 10;
