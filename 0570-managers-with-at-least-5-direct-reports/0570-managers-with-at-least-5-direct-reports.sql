-- Write your PostgreSQL query statement below
select e.name from Employee e 
where id in (
    select managerId from Employee em
    group by em.managerId
    having count(em.managerId) >= 5
)