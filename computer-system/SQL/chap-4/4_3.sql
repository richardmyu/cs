CREATE TABLE ProductMargin (
  product_id CHAR(4) NOT NULL,
  product_name VARCHAR(100) NOT NULL,
  sale_price INTEGER,
  purchase_price INTEGER,
  margin INTEGER,
  PRIMARY KEY(product_id)
);

INSERT INTO
  ProductMargin (
    product_id,
    product_name,
    sale_price,
    purchase_price,
    margin
  )
SELECT
  product_id,
  product_name,
  sale_price,
  purchase_price,
  sale_price - purchase_price
FROM
  Product;
