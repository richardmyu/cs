-- 题目 查找GPA最高值
-- 关键字 高级查询
SELECT
  ROUND(MAX(gpa), 1)
FROM
  user_profile
WHERE
  university = "复旦大学";
