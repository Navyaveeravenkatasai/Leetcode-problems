# Last Login in 2020 in MySQL

**SQL Query (Correct Answer)**
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp LIKE '2020%'
GROUP BY user_id;

**🧩 Step-by-Step Explanation (Detailed)**
**🔹 Step 1: FROM Logins**
FROM Logins


This tells SQL which table to read data from.

The Logins table contains login records of users with:

user_id

time_stamp

🔹 **Step 2: WHERE time_stamp LIKE '2020%'**
WHERE time_stamp LIKE '2020%'


This filters rows before grouping.

It selects only those records where the login happened in year 2020.

'2020%' means:

Starts with 2020

Includes all dates from 2020-01-01 to 2020-12-31

🔹 **Step 3: GROUP BY user_id**
GROUP BY user_id


This groups all login records user-wise.

After this step:

Each group represents one user

All their 2020 logins are collected together

🔹 **Step 4: MAX(time_stamp)**
MAX(time_stamp) AS last_stamp


MAX() is an aggregate function.

It finds the latest date from each user’s group.

This gives the last login time in 2020 for every user.

📌 The alias last_stamp:

Makes the output column name match the LeetCode expected format

🔄 Execution Flow 

SQL executes in this order:

FROM → reads the table

WHERE → filters 2020 records

GROUP BY → groups by user

MAX() → finds latest timestamp per user

SELECT → displays result

# SQL Query
```
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp LIKE '2020%'
GROUP BY user_id;
```