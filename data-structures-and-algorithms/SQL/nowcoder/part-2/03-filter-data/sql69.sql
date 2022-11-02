-- 题目 返回产品并且按照价格排序
-- 关键字 过滤数据
SELECT
  prod_name,
  prod_price
FROM
  Products
WHERE
  prod_price >= 3
  AND prod_price <= 6
ORDER BY
  prod_price;
