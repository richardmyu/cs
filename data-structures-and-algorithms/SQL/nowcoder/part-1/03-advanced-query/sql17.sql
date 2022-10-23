-- 题目 计算男生人数以及平均GPA
-- 关键字 高级查询
-- AVG
SELECT
  COUNT(*) AS male_num,
  ROUND(AVG(gpa), 1) AS avg_gpa
FROM
  user_profile
WHERE
  gender = "male";
