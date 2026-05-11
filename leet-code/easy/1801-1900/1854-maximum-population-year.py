# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of
# the ith person.
#
# The population of some year x is the number of people alive during that year. The ith person is counted in year x's
# population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that
# they die.
#
# Return the earliest year with the maximum population.

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        changes = [0] * 101  # years 1950-2050

        for birth, death in logs:
            changes[birth - 1950] += 1
            changes[death - 1950] -= 1

        max_pop = 0
        current = 0
        answer = 1950

        for i in range(101):
            current += changes[i]

            if current > max_pop:
                max_pop = current
                answer = 1950 + i

        return answer
