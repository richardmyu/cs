-- 题目 返回产品名称和与之相关的订单号
-- 关键字 创建高级联结
SELECT
  P.prod_name,
  O.order_num
FROM
  Products AS P
  LEFT OUTER JOIN OrderItems AS O ON P.prod_id = O.prod_id
ORDER BY
  prod_name;
