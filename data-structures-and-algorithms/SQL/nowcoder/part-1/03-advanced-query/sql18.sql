-- 题目 分组计算练习题
-- 关键字 分组查询
SELECT
  gender,
  university,
  COUNT(*) AS user_num,
  ROUND(AVG(active_days_within_30), 1) AS avg_active_day,
  ROUND(AVG(question_cnt), 1) AS avg_question_cnt
FROM
  user_profile
GROUP BY
  university,
  gender;
