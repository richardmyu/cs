-- 题目 查看学校名称中含北京的用户
SELECT
  device_id,
  age,
  university
FROM
  user_profile
WHERE
  university LIKE "北京%";
