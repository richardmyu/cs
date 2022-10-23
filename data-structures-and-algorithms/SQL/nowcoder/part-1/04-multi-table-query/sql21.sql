-- 题目 浙江大学用户题目回答情况
-- 关键字 多表查询 子查询
SELECT
  QP.device_id,
  QP.question_id,
  QP.result
FROM
  question_practice_detail AS QP
  INNER JOIN user_profile AS UP ON QP.device_id = UP.device_id
WHERE
  university = "浙江大学"
ORDER BY
  question_id;
