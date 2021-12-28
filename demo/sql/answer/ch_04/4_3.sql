CREATE TABLE Product
(product_id      CHAR(4)      NOT NULL,
 product_name    VARCHAR(100) NOT NULL,
 product_type    VARCHAR(32)  NOT NULL,
 sale_price      INTEGER ,
 purchase_price  INTEGER ,
 regist_date     DATE ,
 PRIMARY KEY (product_id));

BEGIN TRANSACTION;
    INSERT INTO Product VALUES ('0001', 'T恤衫', '衣服', 1000, 500, '2008-09-20');
    INSERT INTO Product VALUES ('0002', '打孔器', '办公用品', 500, 320, '2008-09-11');
    INSERT INTO Product VALUES ('0003', '运动T恤', '衣服', 4000, 2800, NULL);
COMMIT;

-- 商品利润表
CREATE TABLE ProductMargin
(product_id     CHAR(4)      NOT NULL,
 product_name   VARCHAR(100) NOT NULL,
 sale_price     INTEGER,
 purchase_price INTEGER,
 margin         INTEGER,
 PRIMARY KEY(product_id));

BEGIN TRANSACTION;
  INSERT INTO ProductMargin (product_id, product_name,sale_price, purchase_price, margin)
  SELECT product_id, product_name, sale_price, purchase_price, sale_price - purchase_price
  FROM Product;
COMMIT;

SELECT * FROM ProductMargin;

/*
 product_id | product_name | sale_price | purchase_price | margin
------------+--------------+------------+----------------+--------
 0001       | T恤衫        |       1000 |            500 |    500
 0002       | 打孔器       |        500 |            320 |    180
 0003       | 运动T恤      |       4000 |           2800 |   1200
*/
