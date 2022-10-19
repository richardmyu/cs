-- 题目 查找学校是北大的学生信息
SELECT
  device_id,
  university
FROM
  user_profile
WHERE
  university = "北京大学";
