-- 题目 按照数量和价格排序
-- 关键字 排序检索数据 排序检索数据
SELECT
  quantity,
  item_price
FROM
  OrderItems
ORDER BY
  quantity DESC,
  item_price DESC;
