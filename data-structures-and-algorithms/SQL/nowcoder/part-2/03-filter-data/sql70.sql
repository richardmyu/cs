-- 题目 返回更多的产品
-- 关键字 过滤数据
SELECT
  DISTINCT order_num
FROM
  OrderItems
WHERE
  quantity >= 100;
