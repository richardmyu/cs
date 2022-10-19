SELECT
  SUM(
    CASE
      WHEN sale_price <= 1000 THEN 1
      ELSE 0
    END
  ) AS low_price,
  SUM(
    CASE
      WHEN sale_price > 1000
      AND sale_price <= 3000 THEN 1
      ELSE 0
    END
  ) AS mid_price,
  SUM(
    CASE
      WHEN sale_price > 3000 THEN 1
      ELSE 0
    END
  ) AS high_price
FROM
  Product;

/*
 low_price | mid_price | high_price
 -----------+-----------+------------
 5 |         1 |          2
 */
