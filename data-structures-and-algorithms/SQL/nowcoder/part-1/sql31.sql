-- 题目 提取博客URL中的用户名
-- 关键字 必会的常用函数 文本函数
SELECT
  device_id,
  SUBSTRING(
    blog_url
    FROM
      11
  ) AS user_name
FROM
  user_submit;
