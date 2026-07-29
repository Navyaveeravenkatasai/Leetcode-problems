-- Write your PostgreSQL query statement below
update Salary set sex = case sex
when 'm' then 'f'
else 'm'
end;