# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6

        actual_sum = sum(nums)
        actual_sq_sum = sum(x * x for x in nums)

        diff = actual_sum - expected_sum  # d - m
        sum_dm = (actual_sq_sum - expected_sq_sum) // diff  # d + m

        duplicate = (diff + sum_dm) // 2
        missing = sum_dm - duplicate

        return [duplicate, missing]
