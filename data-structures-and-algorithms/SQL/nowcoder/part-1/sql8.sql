-- 题目 查找某个年龄段的用户信息
SELECT
  device_id,
  gender,
  age
FROM
  user_profile
WHERE
  age <= 23
  AND age >= 20;
