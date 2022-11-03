-- 题目 打折
-- 关键字 创建计算字段
SELECT
  prod_id,
  prod_price,
  prod_price * 0.9 AS sale_price
FROM
  Products;
