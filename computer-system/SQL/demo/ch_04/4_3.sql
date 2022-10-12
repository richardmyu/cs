INSERT INTO ProductMargin (product_id, product_name,sale_price, purchase_price, margin)
  SELECT product_id, product_name, sale_price, purchase_price, sale_price - purchase_price
  FROM Product;
