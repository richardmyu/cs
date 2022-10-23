-- 题目 查找后多列排序
-- 关键字 基础排序
SELECT
  device_id,
  gpa,
  age
FROM
  user_profile
ORDER BY
  gpa,
  age;
