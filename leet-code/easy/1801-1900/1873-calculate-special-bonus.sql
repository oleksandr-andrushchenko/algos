-- Table: Employees
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | employee_id | int     |
-- | name        | varchar |
-- | salary      | int     |
-- +-------------+---------+
-- employee_id is the primary key (column with unique values) for this table.
-- Each row of this table indicates the employee ID, employee name, and salary.
--
--
-- Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
--
-- Return the result table ordered by employee_id.
--
-- The result format is in the following example.

SELECT employee_id,
       CASE
           WHEN employee_id % 2 = 1
           AND name NOT LIKE 'M%' THEN salary
        ELSE 0
END
AS bonus
FROM Employees
ORDER BY employee_id;