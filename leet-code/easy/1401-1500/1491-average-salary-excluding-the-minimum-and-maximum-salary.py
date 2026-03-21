# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
#
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual
# answer will be accepted.

class Solution:
    def average(self, salary: list[int]) -> float:
        total = sum(salary)
        min_salary = min(salary)
        max_salary = max(salary)

        return (total - min_salary - max_salary) / (len(salary) - 2)
