-- 题目 用where过滤空值练习
-- 关键字 基础操作符
SELECT
  device_id,
  gender,
  age,
  university
FROM
  user_profile
WHERE
  age IS NOT NULL;
