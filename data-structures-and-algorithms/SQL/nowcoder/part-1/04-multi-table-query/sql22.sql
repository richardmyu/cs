-- 题目 统计每个学校的答过题的用户的平均答题数
-- 关键字 多表查询 链接查询
SELECT
  university,
  ROUND(AVG(result_cnt), 4) AS avg_answer_cnt
FROM
  (
    SELECT
      UP.university,
      COUNT(QP.result) AS result_cnt,
      UP.device_id
    FROM
      question_practice_detail AS QP
      INNER JOIN user_profile AS UP ON QP.device_id = UP.device_id
    GROUP BY
      university,
      device_id
  ) AS a
GROUP BY
  university
ORDER BY
  university;
