-- 题目 返回购买 prod_id 为 BR01 的产品的所有顾客的电子邮件 （ 二 ）
-- 关键字 联结表
-- CASE 1
SELECT
  cust_email
FROM
  Customers
WHERE
  cust_id IN (
    SELECT
      cust_id
    FROM
      Orders
    WHERE
      order_num IN(
        SELECT
          order_num
        FROM
          OrderItems
        WHERE
          prod_id = 'BR01'
      )
  );

-- CASE INNER JOIN
SELECT
  C.cust_email
FROM
  Customers AS C
  INNER JOIN Orders AS O ON C.cust_id = O.cust_id
  INNER JOIN OrderItems AS OI ON O.order_num = OI.order_num
WHERE
  OI.prod_id = 'BR01';
