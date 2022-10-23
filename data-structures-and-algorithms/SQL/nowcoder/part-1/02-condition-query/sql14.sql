-- 题目 操作符混合运用
-- 关键字 高级操作符
-- AND OR 组合
SELECT
  device_id,
  gender,
  age,
  university,
  gpa
FROM
  user_profile
WHERE
  (
    university = "山东大学"
    AND gpa > 3.5
  )
  OR (
    university = "复旦大学"
    AND gpa > 3.8
  )
