-- 题目 返回更高价格的产品
-- 关键字 过滤数据
SELECT
  prod_id,
  prod_name
FROM
  Products
WHERE
  prod_price >= 9;
