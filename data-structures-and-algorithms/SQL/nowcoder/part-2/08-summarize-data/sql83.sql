-- 题目 确定已售出产品的总数
-- 关键字 汇总数据
SELECT
  SUM(quantity) AS items_ordered
FROM
  OrderItems;
