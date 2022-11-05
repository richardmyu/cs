-- 题目 返回顾客名称和相关订单号
-- 关键字 联结表
SELECT
  C.cust_name,
  O.order_num
FROM
  Customers AS C
  INNER JOIN Orders AS O ON C.cust_id = O.cust_id
ORDER BY
  cust_name,
  order_num;
