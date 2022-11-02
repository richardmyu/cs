-- 题目 检索供应商名称
-- 关键字 高级数据过滤
SELECT
  vend_name
FROM
  Vendors
WHERE
  vend_country = 'USA'
  AND vend_state = 'CA';
