select stock_name,
SUm(CASE
    WHEN operation="Buy" then -price
    WHEN operation="Sell" then price 
END)
as capital_gain_loss
from stocks
group by stock_name;