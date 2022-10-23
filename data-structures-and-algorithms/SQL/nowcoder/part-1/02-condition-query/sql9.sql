-- 题目 查找除复旦大学的用户信息
-- 关键字 基础操作符
-- NOT
SELECT
  device_id,
  gender,
  age,
  university
FROM
  user_profile
WHERE
  NOT university = "复旦大学";
