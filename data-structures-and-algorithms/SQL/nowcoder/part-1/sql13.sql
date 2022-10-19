-- 题目 Where  in 和 Not in
SELECT
  device_id,
  gender,
  age,
  university,
  gpa
FROM
  user_profile
WHERE
  university IN ("北京大学", "复旦大学", "山东大学");
