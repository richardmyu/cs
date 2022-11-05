-- case 1
SELECT
  product_id,
  product_name,
  product_type,
  sale_price,
  (
    SELECT
      AVG(sale_price)
    FROM
      Product AS P2
    WHERE
      P1.product_type = P2.product_type
  ) AS avg_sale_price
FROM
  Product AS P1;

-- case 2
CREATE VIEW AvgPriceByType AS
SELECT
  product_id,
  product_name,
  product_type,
  sale_price,
  (
    SELECT
      AVG(sale_price)
    FROM
      Product P2
    WHERE
      P1.product_type = P2.product_type
    GROUP BY
      P2.product_type
  ) AS avg_sale_price
FROM
  Product P1;

SELECT
  *
FROM
  AvgPriceByType;
