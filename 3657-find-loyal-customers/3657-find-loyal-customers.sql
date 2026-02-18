# Write your MySQL query statement below
with cte 
    as (select customer_id,sum(CASE WHEN transaction_type = 'purchase' THEN 1 ELSE 0 END) as num_transaction,
    sum(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0 END)/COUNT(DISTINCT transaction_id) as refundrate,
    DATEDIFF(MAX(transaction_date),MIN(transaction_date)) as active
from customer_transactions 
group by customer_id ) 
select customer_id 
from cte 
where num_transaction >= 3 and refundrate < 0.2 and active >= 30 
order by customer_id