BEGIN TRANSACTION;

INSERT INTO
  Product
VALUES
  ('0001', "T恤衫", "衣服", 1000, 500, '2008-09-20');

INSERT INTO
  Product
VALUES
  ('0002', "打孔器", "办公用品", 500, 320, '2008-09-11');

INSERT INTO
  Product
VALUES
  ('0003', "运动T恤", "衣服", 4000, 2800, NULL);

COMMIT;

INSERT INTO
  Product
SELECT
  *
FROM
  Product;

/*
 错误:  重复键违反唯一约束"product_key"
 描述:  键值"(product_id)=(0001)" 已经存在
 */
