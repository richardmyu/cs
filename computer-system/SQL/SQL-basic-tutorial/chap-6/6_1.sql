SELECT
  product_name,
  purchase_price
FROM
  Product
WHERE
  purchase_price NOT IN (500, 2800, 5000);

/*
 product_name | purchase_price
 --------------+----------------
 打孔器       |            320
 擦菜板       |            790
 (2 行记录)
 */
SELECT
  product_name,
  purchase_price
FROM
  Product
WHERE
  purchase_price NOT IN (500, 2800, 5000, NULL);

/*
 product_name | purchase_price
 --------------+----------------
 (0 行记录)
 */
