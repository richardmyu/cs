-- 题目 高级操作符练习(1)
-- 关键字 高级操作符
SELECT
  device_id,
  gender,
  age,
  university,
  gpa
FROM
  user_profile
WHERE
  gender = "male"
  AND gpa > 3.5;
