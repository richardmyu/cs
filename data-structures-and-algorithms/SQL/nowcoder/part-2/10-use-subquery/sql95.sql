-- 题目 从 Products 表中检索所有的产品名称以及对应的销售总数
-- 关键字 使用子查询
SELECT
  prod_name,
  (
    SELECT
      SUM(quantity) AS quant
    FROM
      OrderItems AS OI
    WHERE
      OI.prod_id = P.prod_id
  ) AS quant_sold
FROM
  Products AS P;
