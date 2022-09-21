SELECT CASE WHEN SP.shop_id IS NOT NULL THEN SP.shop_id ELSE '不确定' END,
       CASE WHEN SP.shop_name IS NOT NULL THEN SP.shop_name ELSE '不确定' END,
       P.product_id,
       P.product_name,
       P.sale_price
  FROM ShopProduct AS SP RIGHT OUTER JOIN Product AS P
    ON SP.product_id = P.product_id
ORDER BY shop_id;
