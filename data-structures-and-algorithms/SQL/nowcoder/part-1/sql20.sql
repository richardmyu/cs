-- 题目 分组排序练习题
-- 关键字 分组查询
SELECT
  university,
  ROUND(AVG(question_cnt), 4) AS avg_question_cnt
FROM
  user_profile
GROUP BY
  university
ORDER BY
  avg_question_cnt;
