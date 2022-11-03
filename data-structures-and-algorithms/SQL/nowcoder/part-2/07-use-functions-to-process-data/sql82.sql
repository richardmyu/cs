-- 题目 返回 2020 年 1 月的所有订单的订单号和订单日期
-- 关键字 使用函数处理数据
SELECT
  order_num,
  order_date
FROM
  Orders
WHERE
  order_date >= '2020-01-01 00:00:00'
  AND order_date <= '2020-02-01 00:00:00'
ORDER BY
  order_date;
