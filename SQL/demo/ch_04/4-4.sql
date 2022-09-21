-- 将运动 T 恤的销售单价从 4000 日元下调至 3000 日元。
-- 根据上述结果再次计算运动 T 恤的利润。

UPDATE ProductMargin
  SET sale_price = sale_price - 1000,
      margin = sale_price - purchase_price
 WHERE product_name = '运动T恤';

SELECT * FROM ProductMargin;

/*
 product_id | product_name | sale_price | purchase_price | margin
------------+--------------+------------+----------------+--------
 0001       | T恤衫        |       1000 |            500 |    500
 0002       | 打孔器       |        500 |            320 |    180
 0003       | 运动T恤      |       3000 |           2800 |    200
*/
