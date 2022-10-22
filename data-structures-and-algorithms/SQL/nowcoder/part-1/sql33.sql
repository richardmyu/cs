-- 题目 找出每个学校GPA最低的同学
-- 关键字 必会的常用函数 窗口函数
SELECT
  UP.device_id,
  UP.university,
  ROUND(GP.gpa, 4) AS gpa
FROM
  user_profile AS UP
  INNER JOIN (
    SELECT
      university,
      MIN(gpa) AS gpa
    FROM
      user_profile
    GROUP BY
      university
  ) AS GP ON UP.university = GP.university
  AND UP.gpa = GP.gpa
ORDER BY
  university;
