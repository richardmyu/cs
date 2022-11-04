-- 题目 每个供应商成本最低的产品
-- 关键字 分组数据
SELECT
  vend_id,
  MIN(prod_price) AS cheapest_item
FROM
  Products
GROUP BY
  vend_id
ORDER BY
  cheapest_item;
