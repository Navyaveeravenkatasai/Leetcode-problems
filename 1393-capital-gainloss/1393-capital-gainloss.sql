select stock_name,(Sellprice - Buyprice) as capital_gain_loss
from 
(
select stock_name ,sum(case when operation = "Buy" then price end) as Buyprice,
sum(case when operation = "Sell" then price end) as Sellprice
from Stocks
group by stock_name
) t