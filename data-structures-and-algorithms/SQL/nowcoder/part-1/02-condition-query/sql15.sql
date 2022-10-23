-- 题目 查看学校名称中含北京的用户
-- 关键字 高级操作符
-- LIKE SUBSTRING
-- CASE1 - LIKE
SELECT
  device_id,
  age,
  university
FROM
  user_profile
WHERE
  university LIKE "北京%";

-- CASE2 - SUBSTRING
SELECT
  device_id,
  age,
  university
FROM
  user_profile
WHERE
  SUBSTRING(
    university
    FROM
      1 FOR 2
  ) = "北京";
