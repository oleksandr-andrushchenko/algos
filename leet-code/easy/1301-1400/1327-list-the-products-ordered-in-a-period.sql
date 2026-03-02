-- Table: Products
--
-- +------------------+---------+
-- | Column Name      | Type    |
-- +------------------+---------+
-- | product_id       | int     |
-- | product_name     | varchar |
-- | product_category | varchar |
-- +------------------+---------+
-- product_id is the primary key (column with unique values) for this table.
-- This table contains data about the company's products.
--
--
-- Table: Orders
--
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | product_id    | int     |
-- | order_date    | date    |
-- | unit          | int     |
-- +---------------+---------+
-- This table may have duplicate rows.
-- product_id is a foreign key (reference column) to the Products table.
-- unit is the number of products ordered in order_date.
--
--
-- Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.
--
-- Return the result table in any order.

SELECT p.product_name,
       SUM(o.unit) AS unit
FROM Products p
         JOIN Orders o
              ON p.product_id = o.product_id
WHERE o.order_date >= DATE '2020-02-01'
  AND o.order_date < DATE '2020-03-01'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;