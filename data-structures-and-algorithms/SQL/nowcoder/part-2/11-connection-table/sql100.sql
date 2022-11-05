-- 题目 确定最佳顾客的另一种方式 （ 二 ）
-- 关键字 联结表
SELECT
  C.cust_name,
  SUM(OI.item_price * OI.quantity) AS total_price
FROM
  Customers AS C
  INNER JOIN Orders AS O ON C.cust_id = O.cust_id
  INNER JOIN OrderItems AS OI ON O.order_num = OI.order_num
GROUP BY
  cust_name
HAVING
  total_price >= 1000
ORDER BY
  total_price;
