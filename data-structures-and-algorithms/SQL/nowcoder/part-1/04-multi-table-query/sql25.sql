-- 题目 查找山东大学或者性别为男生的信息
-- 关键字 多表查询 组合查询
SELECT
  device_id,
  gender,
  age,
  gpa
FROM
  user_profile
WHERE
  university = "山东大学"
UNION
ALL
SELECT
  device_id,
  gender,
  age,
  gpa
FROM
  user_profile
WHERE
  gender = "male";
