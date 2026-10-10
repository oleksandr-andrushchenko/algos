-- Table: products
--
-- +--------------+------------+
-- | Column Name  | Type       |
-- +--------------+------------+
-- | product_id   | int        |
-- | product_name | varchar    |
-- | description  | varchar    |
-- +--------------+------------+
-- (product_id) is the unique key for this table.
-- Each row in the table represents a product with its unique ID, name, and description.
-- Write a solution to find all products whose description contains a valid serial number pattern. A valid serial number follows these rules:
--
-- It starts with the letters SN (case-sensitive).
-- Followed by exactly 4 digits.
-- It must have a hyphen (-) followed by exactly 4 digits.
-- The serial number must be within the description (it may not necessarily start at the beginning).
-- Return the result table ordered by product_id in ascending order.


SELECT *
FROM products
WHERE description ~ 'SN[0-9]{4}-[0-9]{4}([^0-9]|$)'
ORDER BY product_id;