-- Table: Employee
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
--
--
-- Write a solution to find the employees who earn more than their managers.
--
-- Return the result table in any order.

SELECT e.name AS Employee
FROM Employee e
         JOIN Employee m
              ON e.managerId = m.id
WHERE e.salary > m.salary;