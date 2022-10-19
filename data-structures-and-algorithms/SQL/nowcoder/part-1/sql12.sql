-- 题目 高级操作符练习(2)
SELECT
  device_id,
  gender,
  age,
  university,
  gpa
FROM
  user_profile
WHERE
  university = "北京大学"
  OR gpa > 3.7;
