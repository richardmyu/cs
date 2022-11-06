-- 题目 21 年8月份练题总数
-- 关键字 综合练习
SELECT
  COUNT(*) AS did_cnt,
  SUM(question_item_cnt) AS question_cnt
FROM
  (
    SELECT
      device_id,
      COUNT(question_id) AS question_item_cnt
    FROM
      Question_practice_detail
    WHERE
      EXTRACT(
        MONTH
        FROM
          date
      ) = '08'
    GROUP BY
      device_id
  ) AS a;
