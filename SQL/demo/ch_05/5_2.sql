CREATE VIEW ViewPractice5_1 (product_name, sale_price, regist_date)
AS
SELECT product_name, sale_price, regist_date
  FROM Product
  WHERE sale_price >= 1000 AND regist_date = '2009-09-20';

INSERT INTO ViewPractice5_1 VALUES ('刀子',300,'2009-11-02');

/*
错误:  null value in column "product_id" of relation "product" violates not-null constraint
描述:  失败, 行包含(null, 刀子, null, 300, null, 2009-11-02).
*/
