-- 题目 返回所有价格在 3 美元到 6 美元之间的产品的名称和价格
-- 关键字 高级数据过滤
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
