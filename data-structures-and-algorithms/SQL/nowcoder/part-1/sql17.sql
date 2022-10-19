-- 题目 计算男生人数以及平均GPA
SELECT
  COUNT(*) AS male_num,
  ROUND(AVG(gpa), 1) AS avg_gpa
FROM
  user_profile
WHERE
  gender = "male";
