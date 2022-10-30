-- 题目 对顾客ID和日期排序
-- 关键字 排序检索数据 排序检索数据
SELECT
  cust_id,
  order_num
FROM
  Orders
ORDER BY
  cust_id,
  order_date DESC;
