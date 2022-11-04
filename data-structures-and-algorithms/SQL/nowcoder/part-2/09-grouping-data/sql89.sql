-- 题目 计算总和
-- 关键字 分组数据
SELECT
  order_num,
  SUM(item_price * quantity) AS total_price
FROM
  OrderItems
GROUP BY
  order_num
HAVING
  total_price >= 1000
ORDER BY
  order_num;
