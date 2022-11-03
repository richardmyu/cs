-- 题目 检索产品名称和描述 （ 三 ）
-- 关键字 用通配符进行过滤
SELECT
  prod_name,
  prod_desc
FROM
  Products
WHERE
  prod_desc LIKE '%toy%'
  AND prod_desc LIKE '%carrots%';
