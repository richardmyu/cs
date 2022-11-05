-- 题目  将两个 SELECT 语句结合起来（一）
-- 关键字 组合查询
SELECT
  prod_id,
  quantity
FROM
  OrderItems
WHERE
  quantity = 100
UNION
SELECT
  prod_id,
  quantity
FROM
  OrderItems
WHERE
  prod_id LIKE 'BNBG%'
ORDER BY
  prod_id;
