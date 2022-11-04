-- 题目 返回订单数量总和不小于100的所有订单的订单号
-- 关键字 分组数据
SELECT
  order_num
FROM
  OrderItems
GROUP BY
  order_num
HAVING
  SUM(quantity) >= 100
ORDER BY
  order_num;
