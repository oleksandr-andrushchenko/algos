# You are given an integer array nums of length n.
#
# The score of an index i is defined as the number of indices j such that:
#
# i < j < n, and
# nums[i] and nums[j] have different parity (one is even and the other is odd).
# Return an integer array answer of length n, where answer[i] is the score of index i.

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        answer = [0] * len(nums)
        evens = odds = 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 0:
                answer[i] = odds
                evens += 1
            else:
                answer[i] = evens
                odds += 1

        return answer
