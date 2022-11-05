SELECT
  product_id,
  product_name,
  sale_price,
  MAX (sale_price) OVER (
    ORDER BY
      product_id
  ) AS current_max_price
FROM
  Product;

/*
 product_id | product_name | sale_price | current_max_price
 ------------+--------------+------------+-------------------
 0001       | T恤衫        |       1000 |              1000
 0002       | 打孔器       |        500 |              1000
 0003       | 运动T恤      |       4000 |              4000
 0004       | 菜刀         |       3000 |              4000
 0005       | 高压锅       |       6800 |              6800
 0006       | 叉子         |        500 |              6800
 0007       | 擦菜板       |        880 |              6800
 0008       | 圆珠笔       |        100 |              6800
 */
