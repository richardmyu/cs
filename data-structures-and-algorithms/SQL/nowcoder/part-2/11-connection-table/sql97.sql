-- 题目 返回顾客名称和相关订单号以及每个订单的总价
-- 关键字 联结表
SELECT
  C.cust_name,
  O.order_num,
  (OI.quantity * OI.item_price) AS OrderTotal
FROM
  Customers AS C
  INNER JOIN Orders AS O ON C.cust_id = O.cust_id
  INNER JOIN OrderItems AS OI ON O.order_num = OI.order_num
ORDER BY
  cust_name,
  order_num;
