-- 题目 返回购买价格为 10 美元或以上产品的顾客列表
-- 关键字 使用子查询
SELECT
  cust_id
FROM
  Orders
WHERE
  order_num in (
    SELECT
      order_num
    FROM
      OrderItems
    WHERE
      item_price >= 10
  );
