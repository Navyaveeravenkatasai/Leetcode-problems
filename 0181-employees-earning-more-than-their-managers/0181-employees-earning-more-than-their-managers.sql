select e.name as Employee
from Employee e
JOIN employee m
on e.managerID = m.id
where e.salary > m.salary