SELECT product_id,
       product_name,
       product_type,
       sale_price,
       (SELECT AVG(sale_price)
         FROM Product AS P2
         WHERE P1.product_type = P2.product_type
       ) AS avg_sale_price
 FROM Product AS P1;


