SELECT
  product_id,
  SUM(product_name) -- 本SELECT语句中存在错误。
FROM
  Product
GROUP BY
  product_type
WHERE
  regist_date > '2009-09-01';

-- GROUP BY 应该在 WHERE 后面
-- SUM 只能用于数字类型
-- 存在 GROUP BY 子句中未指定的列（product_id）
