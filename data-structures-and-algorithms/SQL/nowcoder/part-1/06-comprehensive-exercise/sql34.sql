-- 题目 统计复旦用户8月练题情况
-- 关键字 综合练习
TODO: 待解决
SELECT
  UP.device_id,
  UP.university,
  UP.question_cnt,
  COUNT(*) AS right_question_cnt
FROM
  (
    SELECT
      device_id,
      university,
      question_cnt
    FROM
      user_profile
    WHERE
      university = "复旦大学"
  ) AS UP
  INNER JOIN (
    SELECT
      device_id,
      result
    FROM
      question_practice_detail
    WHERE
      SUBSTRING(
        date
        FROM
          6 FOR 2
      ) = "08"
  ) AS QD ON UP.device_id = QD.device_id
GROUP BY
  device_id;
