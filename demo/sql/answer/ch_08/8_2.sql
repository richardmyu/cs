SELECT regist_date,sale_price,
       SUM(sale_price) OVER (ORDER BY sale_price)
  FROM Product
ORDER BY regist_date;
