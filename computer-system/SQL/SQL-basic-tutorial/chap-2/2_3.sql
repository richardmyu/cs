-- case 1
SELECT
  product_name,
  sale_price,
  purchase_price
FROM
  Product
WHERE
  sale_price - purchase_price >= 500;

-- case 2
SELECT
  product_name,
  sale_price,
  purchase_price
FROM
  Product
WHERE
  sale_price - 500 >= purchase_price;

-- case 3
SELECT
  product_name,
  sale_price,
  purchase_price
FROM
  Product
WHERE
  sale_price >= purchase_price + 500;

-- case 4
SELECT
  product_name,
  sale_price,
  purchase_price
FROM
  Product
WHERE
  NOT sale_price - purchase_price < 500;
