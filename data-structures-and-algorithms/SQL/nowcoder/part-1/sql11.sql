-- 题目 高级操作符练习(1)
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
