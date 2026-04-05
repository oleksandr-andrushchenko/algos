-- Table: Users
--
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | account      | int     |
-- | name         | varchar |
-- +--------------+---------+
-- account is the primary key (column with unique values) for this table.
-- Each row of this table contains the account number of each user in the bank.
-- There will be no two users having the same name in the table.
--
--
-- Table: Transactions
--
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | trans_id      | int     |
-- | account       | int     |
-- | amount        | int     |
-- | transacted_on | date    |
-- +---------------+---------+
-- trans_id is the primary key (column with unique values) for this table.
-- Each row of this table contains all changes made to all accounts.
-- amount is positive if the user received money and negative if they transferred money.
-- All accounts start with a balance of 0.
--
--
-- Write a solution to report the name and balance of users with a balance higher than 10000. The balance of an account
-- is equal to the sum of the amounts of all transactions involving that account.
--
-- Return the result table in any order.

SELECT u.name,
       SUM(t.amount) AS balance
FROM Users u
         JOIN Transactions t
              ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;