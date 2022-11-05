-- 题目 确定哪些订单购买了 prod_id 为 BR01 的产品 （ 二 ）
-- 关键字 联结表
SELECT
  cust_id,
  order_date
FROM
  Orders
WHERE
  order_num IN (
    SELECT
      order_num
    FROM
      OrderItems
    WHERE
      prod_id = 'BR01'
  )
ORDER BY
  order_date;
