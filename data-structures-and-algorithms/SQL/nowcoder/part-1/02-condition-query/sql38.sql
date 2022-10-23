-- 题目 查找后降序排列
-- 关键字 基础排序
SELECT
  device_id,
  gpa,
  age
FROM
  user_profile
ORDER BY
  gpa DESC,
  age DESC;
