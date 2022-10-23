-- 题目 分组过滤练习题
-- 关键字 分组查询
SELECT
  university,
  ROUND(AVG(question_cnt), 3) AS avg_question_cnt,
  ROUND(AVG(answer_cnt), 3) AS avg_answer_cnt
FROM
  user_profile
GROUP BY
  university
HAVING
  AVG(question_cnt) < 5
  OR AVG(answer_cnt) < 20;
