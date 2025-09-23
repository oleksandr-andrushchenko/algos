-- Write a query to print all prime numbers less than or equal to .
-- Print your result on a single line, and use the ampersand () character as your separator (instead of a space).
--
-- For example, the output for all prime numbers  would be:
--
-- 2&3&5&7

WITH RECURSIVE nums AS ( -- Generate numbers from 2 to N
    SELECT 2 AS n
    UNION ALL
    SELECT n + 1
    FROM nums
    WHERE n < 1000)
SELECT GROUP_CONCAT(n SEPARATOR '&') AS primes
FROM nums
WHERE NOT EXISTS ( -- Filter out non-primes
    SELECT 1
    FROM nums AS d
    WHERE d.n < nums.n
      AND nums.n % d.n = 0
      AND d.n > 1);