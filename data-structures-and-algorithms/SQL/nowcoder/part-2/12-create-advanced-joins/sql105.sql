-- 题目 列出供应商及其可供产品的数量
-- 关键字 创建高级联结
SELECT
  V.vend_id,
  COUNT(P.vend_id) AS prod_id
FROM
  Vendors AS V
  LEFT OUTER JOIN Products AS P ON V.vend_id = P.vend_id
GROUP BY
  V.vend_id
ORDER BY
  V.vend_id;
