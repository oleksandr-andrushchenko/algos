# You are given two integer arrays nums and divisors.
#
# The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].
#
# Return the integer divisors[i] with the maximum divisibility score. If multiple integers have the maximum score, return
# the smallest one.

from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        best_divisor = divisors[0]
        best_score = -1

        for divisor in divisors:
            score = 0

            for num in nums:
                if num % divisor == 0:
                    score += 1

            if score > best_score or (
                    score == best_score and divisor < best_divisor
            ):
                best_score = score
                best_divisor = divisor

        return best_divisor
