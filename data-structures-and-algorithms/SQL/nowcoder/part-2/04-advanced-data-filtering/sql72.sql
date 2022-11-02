-- 题目 检索并列出已订购产品的清单
-- 关键字 高级数据过滤
SELECT
  order_num,
  prod_id,
  quantity
FROM
  OrderItems
WHERE
  prod_id IN('BR01', 'BR02', 'BR03')
  AND quantity >= 100;
