-- 题目 返回每个顾客不同订单的总金额
-- 关键字 使用子查询
SELECT
  cust_id,
  (
    SELECT
      SUM(item_price * quantity) AS total_ordered
    FROM
      OrderItems AS OI
    WHERE
      O.order_num = OI.order_num
  ) AS total_ordered
FROM
  Orders AS O
ORDER BY
  total_ordered DESC;
