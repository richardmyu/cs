-- 题目 查看不同年龄段的用户明细
-- 关键字 必会的常用函数 条件函数
SELECT
  device_id,
  gender,
  CASE
    WHEN age BETWEEN 20
    AND 24 THEN '20-24岁'
    WHEN age BETWEEN 25
    AND 100 THEN '25岁及以上'
    ELSE '其他'
  END AS age_cut
FROM
  user_profile;
