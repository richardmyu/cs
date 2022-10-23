-- 题目 查找学校是北大的学生信息
-- 关键字 基础操作符
-- WHERE
SELECT
  device_id,
  university
FROM
  user_profile
WHERE
  university = "北京大学";
