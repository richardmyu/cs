-- 题目 计算25岁以上和以下的用户数量
-- 关键字 必会的常用函数 条件函数
-- 重点：
-- case and bewteen
SELECT
  CASE
    WHEN age BETWEEN 0
    AND 24 THEN '25岁以下'
    WHEN age BETWEEN 25
    AND 100 THEN '25岁及以上'
    ELSE '25岁以下'
  END AS age_cut,
  COUNT(*) AS number
FROM
  user_profile
GROUP BY
  age_cut;
