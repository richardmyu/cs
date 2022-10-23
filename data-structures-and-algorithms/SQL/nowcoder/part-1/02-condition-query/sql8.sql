-- 题目 查找某个年龄段的用户信息
-- 关键字 基础操作符
-- AND BETWEEN
-- CASE1 - AND
SELECT
  device_id,
  gender,
  age
FROM
  user_profile
WHERE
  age <= 23
  AND age >= 20;

-- CASE2 - BETWEEN
SELECT
  device_id,
  gender,
  age
FROM
  user_profile
WHERE
  age BETWEEN 20
  AND 23;
