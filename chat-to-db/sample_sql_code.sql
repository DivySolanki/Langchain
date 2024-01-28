
SELECT stock_quantity FROM t_shirts 
WHERE brand = 'Nike' AND color = 'White' AND size = 'XL'

SELECT * FROM t_shirts 
WHERE brand = 'Nike' AND color = 'White' AND size = 'XL'

SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'

select sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id

SELECT SUM(stock_quantity) FROM t_shirts 
WHERE brand = 'Levi' AND color = 'White'

SELECT sum(stock_quantity) FROM t_shirts 
WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'