/*****************
 *   Product
 ****************/
/*
 +------------+--------------+--------------+------------+----------------+-------------+
 | product_id | product_name | product_type | sale_price | purchase_price | regist_date |
 +------------+--------------+--------------+------------+----------------+-------------+
 | 0001       | T恤          | 衣服         |       1000 |            500 | 2009-09-20  |
 | 0002       | 打孔器       | 办公用品     |        500 |            320 | 2009-09-11  |
 | 0003       | 运动T恤      | 衣服         |       4000 |           2800 | NULL        |
 | 0004       | 菜刀         | 厨房用具     |       3000 |           2800 | 2009-09-20  |
 | 0005       | 高压锅       | 厨房用具     |       6800 |           5000 | 2009-01-15  |
 | 0006       | 叉子         | 厨房用具     |        500 |           NULL | 2009-09-20  |
 | 0007       | 擦菜板       | 厨房用具     |        880 |            790 | 2008-04-28  |
 | 0008       | 圆珠笔       | 办公用品     |        100 |           NULL | 2009-11-11  |
 +------------+--------------+--------------+------------+----------------+-------------+
 */
DROP TABLE IF EXISTS Product;

CREATE TABLE Product (
  product_id CHAR(4) NOT NULL,
  product_name VARCHAR(100) NOT NULL,
  product_type VARCHAR(32) NOT NULL,
  sale_price INTEGER,
  purchase_price INTEGER,
  regist_date DATE,
  PRIMARY KEY (product_id)
);

-- BEGIN TRANSACTION;
START TRANSACTION;

INSERT INTO
  Product
VALUES
  ('0001', 'T恤衫', '衣服', 1000, 500, '2009-09-20');

INSERT INTO
  Product
VALUES
  ('0002', '打孔器', '办公用品', 500, 320, '2009-09-11');

INSERT INTO
  Product
VALUES
  ('0003', '运动T恤', '衣服', 4000, 2800, NULL);

INSERT INTO
  Product
VALUES
  ('0004', '菜刀', '厨房用具', 3000, 2800, '2009-09-20');

INSERT INTO
  Product
VALUES
  ('0005', '高压锅', '厨房用具', 6800, 5000, '2009-01-15');

INSERT INTO
  Product
VALUES
  ('0006', '叉子', '厨房用具', 500, NULL, '2009-09-20');

INSERT INTO
  Product
VALUES
  ('0007', '擦菜板', '厨房用具', 880, 790, '2008-04-28');

INSERT INTO
  Product
VALUES
  ('0008', '圆珠笔', '办公用品', 100, NULL, '2009-11-11');

COMMIT;

/*****************
 *   SampleMath
 ****************/
DROP TABLE IF EXISTS SampleMath;

CREATE TABLE SampleMath (m NUMERIC (10, 3), n INTEGER, p INTEGER);

-- BEGIN TRANSACTION;
START TRANSACTION;

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (500, 0, NULL);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (-180, 0, NULL);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (NULL, NULL, NULL);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (NULL, 7, 3);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (NULL, 5, 2);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (NULL, 4, NULL);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (8, NULL, 3);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (2.27, 1, NULL);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (5.555, 2, NULL);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (NULL, 1, NULL);

INSERT INTO
  SampleMath(m, n, p)
VALUES
  (8.76, NULL, NULL);

COMMIT;

/*****************
 *   SampleStr
 ****************/
CREATE TABLE SampleStr (
  str1 VARCHAR(40),
  str2 VARCHAR(40),
  str3 VARCHAR(40)
);

START TRANSACTION;

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('opx', 'rt', NULL);

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('abc', 'def', NULL);

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('山田', '太郎', '是我');

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('aaa', NULL, NULL);

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  (NULL, 'xyz', NULL);

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('@!#$%', NULL, NULL);

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('ABC', NULL, NULL);

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('aBC', NULL, NULL);

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('abc太郎', 'abc', 'ABC');

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('abcdefabc', 'abc', 'ABC');

INSERT INTO
  SampleStr (str1, str2, str3)
VALUES
  ('micmic', 'i', 'I');

COMMIT;

/*****************
 *   SampleLike
 ****************/
CREATE TABLE SampleLike (
  strcol VARCHAR(6) NOT NULL,
  PRIMARY KEY (strcol)
);

START TRANSACTION;

INSERT INTO
  SampleLike (strcol)
VALUES
  ('abcddd');

INSERT INTO
  SampleLike (strcol)
VALUES
  ('dddabc');

INSERT INTO
  SampleLike (strcol)
VALUES
  ('abdddc');

INSERT INTO
  SampleLike (strcol)
VALUES
  ('abcdd');

INSERT INTO
  SampleLike (strcol)
VALUES
  ('ddabc');

INSERT INTO
  SampleLike (strcol)
VALUES
  ('abddc');

COMMIT;

/*****************
 *   ShopProduct
 ****************/
CREATE TABLE ShopProduct (
  shop_id CHAR(4) NOT NULL,
  shop_name VARCHAR(200) NOT NULL,
  product_id CHAR(4) NOT NULL,
  quantity INTEGER NOT NULL,
  PRIMARY KEY (shop_id, product_id)
);

START TRANSACTION;

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000A', '东京', '0001', 30);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000A', '东京', '0002', 50);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000A', '东京', '0003', 15);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000B', '名古屋', '0002', 30);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000B', '名古屋', '0003', 120);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000B', '名古屋', '0004', 20);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000B', '名古屋', '0006', 10);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000B', '名古屋', '0007', 40);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000C', '大阪', '0003', 20);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000C', '大阪', '0004', 50);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000C', '大阪', '0006', 90);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000C', '大阪', '0007', 70);

INSERT INTO
  ShopProduct (shop_id, shop_name, product_id, quantity)
VALUES
  ('000D', '福冈', '0001', 100);

COMMIT;
