-- 题目 找出每个学校GPA最低的同学
-- 关键字 必会的常用函数 窗口函数
-- 表连接实现
-- SELECT
--   UP.device_id,
--   UP.university,
--   ROUND(GP.gpa, 4) AS gpa
-- FROM
--   user_profile AS UP
--   INNER JOIN (
--     SELECT
--       university,
--       MIN(gpa) AS gpa
--     FROM
--       user_profile
--     GROUP BY
--       university
--   ) AS GP ON UP.university = GP.university
--   AND UP.gpa = GP.gpa
-- ORDER BY
--   university;
SELECT
  device_id,
  university,
  ROUND(gpa, 4) AS gpa
FROM
  (
    SELECT
      device_id,
      university,
      gpa,
      ROW_NUMBER () OVER (
        PARTITION BY university
        ORDER BY
          gpa
      ) AS ranking
    FROM
      user_profile
  ) AS a
WHERE
  ranking = 1;
