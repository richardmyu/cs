-- 题目 统计每种性别的人数
-- 关键字 必会的常用函数 文本函数
SELECT
  SUBSTRING(
    profile
    FROM
      15
  ) AS gender,
  COUNT(*) AS number
FROM
  user_submit
GROUP BY
  gender;
