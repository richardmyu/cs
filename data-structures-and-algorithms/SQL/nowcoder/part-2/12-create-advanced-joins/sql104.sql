-- 题目 返回产品名称和每一项产品的总订单数
-- 关键字 创建高级联结
SELECT
  P.prod_name,
  COUNT(O.order_num) AS orders
FROM
  Products AS P
  LEFT OUTER JOIN OrderItems AS O ON P.prod_id = O.prod_id
GROUP BY
  prod_name
ORDER BY
  prod_name;
