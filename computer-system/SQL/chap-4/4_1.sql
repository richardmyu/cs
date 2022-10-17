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

SELECT * FROM Product;

/*
 product_id | product_name | product_type | sale_price | purchase_price | regist_date
 ------------+--------------+--------------+------------+----------------+-------------
 0001       | T恤衫        | 衣服         |       1000 |            500 | 2008-09-20
 0002       | 打孔器       | 办公用品     |        500 |            320 | 2008-09-11
 0003       | 运动T恤      | 衣服         |       4000 |           2800 |
*/
