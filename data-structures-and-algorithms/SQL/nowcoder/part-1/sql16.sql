-- 题目 查找GPA最高值
SELECT
  ROUND(MAX(gpa), 1)
FROM
  user_profile
WHERE
  university = "复旦大学";
