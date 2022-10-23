-- 题目 截取出年龄
-- 关键字 必会的常用函数 文本函数
SELECT
  SUBSTRING(
    profile
    FROM
      12 FOR 2
  ) AS age,
  COUNT(*) AS number
FROM
  user_submit
GROUP BY
  age;
