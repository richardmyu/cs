SELECT
  regist_date,
  product_name,
  sale_price,
  SUM(sale_price) OVER (
    ORDER BY
      sale_price
  )
FROM
  Product
ORDER BY
  regist_date;

-- regist_date 为 NULL 时，将该记录放在最前显示
SELECT
  regist_date,
  product_name,
  sale_price,
  SUM(sale_price) OVER (
    ORDER BY
      regist_date NULLS FIRST
  ) AS current_sum_price
FROM
  Product;
