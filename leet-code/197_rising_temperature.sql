-- Table: Weather
--
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the column with unique values for this table.
-- There are no different rows with the same recordDate.
-- This table contains information about the temperature on a certain day.
--
--
-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
--
-- Return the result table in any order.

SELECT w2.id
FROM Weather w1
         JOIN Weather w2
              ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
WHERE w2.temperature > w1.temperature