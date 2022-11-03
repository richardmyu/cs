-- 题目 别名
-- 关键字 创建计算字段
SELECT
  vend_id,
  vend_name AS vname,
  vend_address AS vaddress,
  vend_city AS vcity
FROM
  Vendors
ORDER BY
  vname;
