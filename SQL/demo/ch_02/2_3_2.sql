SELECT product_name,sale_price,purchase_price
  FROM Product
 WHERE NOT sale_price - purchase_price < 500;
