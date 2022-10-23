-- 题目 统计每个用户的平均刷题数
-- 关键字 多表查询 链接查询
SELECT
  university,
  difficult_level,
  ROUND(AVG(cnt), 4) AS avg_answer_cnt
FROM
  user_profile AS UP
  INNER JOIN (
    SELECT
      QP.device_id,
      QD.difficult_level,
      COUNT(*) AS cnt
    FROM
      question_practice_detail AS QP
      INNER JOIN question_detail AS QD ON QP.question_id = QD.question_id
    GROUP BY
      difficult_level,
      device_id
  ) AS QPD ON UP.device_id = QPD.device_id
WHERE
  university = "山东大学"
GROUP BY
  university,
  difficult_level;
