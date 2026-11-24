# You are given an integer array nums and an integer target.
#
# A pair of distinct indices (i, j) is valid if:
#
# nums[i] + nums[j] == target
# nums[i] > nums[j]
# Return a valid pair [i, j] whose product nums[i] * nums[j] is maximum among all valid pairs. If no valid pair exists,
# return [-1, -1].
#
# If multiple valid pairs achieve the maximum product, you may return any of them.

class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        best_product = float("-inf")
        answer = [-1, -1]

        for i, num in enumerate(nums):
            other = target - num

            if other != num and other in seen:
                product = num * other

                if product > best_product:
                    best_product = product
                    j = seen[other]
                    answer = [i, j] if num > other else [j, i]

            seen[num] = i

        return answer
