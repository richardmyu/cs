-- 题目 查找年龄大于24岁的用户信息
SELECT
  device_id,
  gender,
  age,
  university
FROM
  user_profile
WHERE
  age > 24;
