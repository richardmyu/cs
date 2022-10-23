-- 题目 计算用户8月每天的练题数量
-- 关键字 必会的常用函数 日期函数
-- 思路
-- 先过滤非 8 月数据
-- 再截取 日 数据计数
SELECT
  EXTRACT(
    DAY
    FROM
      date
  ) AS day,
  COUNT(*) AS question_cnt
FROM
  question_practice_detail
WHERE
  date BETWEEN "2021-08-01"
  AND "2021-08-31"
GROUP BY
  day;
