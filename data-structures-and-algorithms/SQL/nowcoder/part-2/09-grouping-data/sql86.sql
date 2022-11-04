-- 题目 返回每个订单号各有多少行数
-- 关键字 分组数据
SELECT
  order_num,
  COUNT(order_num) AS order_lines
FROM
  OrderItems
GROUP BY
  order_num
ORDER BY
  order_lines;
