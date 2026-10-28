-- Table: prompts
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- | prompt      | varchar |
-- | tokens      | int     |
-- +-------------+---------+
-- (user_id, prompt) is the primary key (unique value) for this table.
-- Each row represents a prompt submitted by a user to an AI system along with the number of tokens consumed.
-- Write a solution to analyze AI prompt usage patterns based on the following requirements:
--
-- For each user, calculate the total number of prompts they have submitted.
-- For each user, calculate the average tokens used per prompt (Rounded to 2 decimal places).
-- Only include users who have submitted at least 3 prompts.
-- Only include users who have submitted at least one prompt with tokens greater than their own average token usage.
-- Return the result table ordered by average tokens in descending order, and then by user_id in ascending order.

SELECT user_id,
       COUNT(*)              AS prompt_count,
       ROUND(AVG(tokens), 2) AS avg_tokens
FROM prompts
GROUP BY user_id
HAVING COUNT(*) >= 3
   AND MAX(tokens) > AVG(tokens)
ORDER BY avg_tokens DESC, user_id ASC;