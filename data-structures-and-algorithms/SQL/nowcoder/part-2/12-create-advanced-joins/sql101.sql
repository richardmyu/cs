-- 题目 检索每个顾客的名称和所有的订单号 （ 一 ）
-- 关键字 创建高级联结
SELECT
  C.cust_name,
  O.order_num
FROM
  Customers AS C
  INNER JOIN Orders AS O ON C.cust_id = O.cust_id
ORDER BY
  cust_name;
