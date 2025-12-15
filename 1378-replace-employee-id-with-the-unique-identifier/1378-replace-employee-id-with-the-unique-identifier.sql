select emp.unique_id,e.name from 
Employees e
LEFT JOIN EmployeeUNI emp on
e.id = emp.id