-- 题目 纠错3
-- 关键字 分组数据
SELECT
  order_num,
  COUNT(*) AS items
FROM
  OrderItems
GROUP BY
  order_num
HAVING
  items >= 3
ORDER BY
  items,
  order_num;
