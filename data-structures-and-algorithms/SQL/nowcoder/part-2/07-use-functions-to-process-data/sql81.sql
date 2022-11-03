-- 题目 顾客登录名
-- 关键字 使用函数处理数据
SELECT
  cust_id,
  cust_name,
  UPPER(
    CONCAT(
      SUBSTRING(
        cust_name
        FROM
          1 FOR 2
      ),
      SUBSTRING(
        cust_city
        FROM
          1 FOR 3
      )
    )
  ) AS user_login
FROM
  Customers;
