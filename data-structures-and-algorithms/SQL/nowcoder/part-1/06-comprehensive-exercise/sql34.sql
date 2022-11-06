-- 题目 统计复旦用户8月练题情况
-- 关键字 综合练习
SELECT
  UPF.device_id,
  UPF.university,
  CASE
    b.question_cnt
    WHEN b.question_cnt THEN 0
    ELSE NULL
  END AS b.question_cnt,
  CASE
    b.right_question_cnt
    WHEN b.right_question_cnt THEN 0
    ELSE NULL
  END AS b.right_question_cnt
FROM
  user_profile AS UPF
  INNER JOIN (
    SELECT
      device_id,
      university,
      COUNT(result) AS question_cnt,
      SUM(result_value) AS right_question_cnt
    FROM
      (
        SELECT
          UP.device_id,
          UP.university,
          QPD.result,
          CASE
            QPD.result
            WHEN 'right' THEN 1
            WHEN 'wrong' THEN 0
            ELSE NULL
          END AS result_value
        FROM
          question_practice_detail AS QPD
          INNER JOIN user_profile UP ON QPD.device_id = UP.device_id
        WHERE
          UP.device_id IN (
            SELECT
              device_id
            FROM
              user_profile
            WHERE
              university = "复旦大学"
          )
          AND SUBSTRING(
            date
            FROM
              6 FOR 2
          ) = "08"
      ) AS a
  ) AS b ON UPF.device_id = b.device_id
WHERE
  university = "复旦大学";
