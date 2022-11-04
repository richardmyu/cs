-- 题目 返回购买 prod_id 为 BR01 的产品的所有顾客的电子邮件 （ 一 ）
-- 关键字 使用子查询
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
