# You are given an integer array nums.
#
# You start with an empty array ans. Repeat the following operation until nums is empty:
#
# Identify all distinct values currently present in nums.
# Remove one occurrence of every distinct value currently in nums, and append those values to ans in ascending order.
# Return the array ans.

from collections import Counter


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        active = sorted(counts)
        ans = []

        while active:
            next_active = []

            for num in active:
                ans.append(num)
                counts[num] -= 1

                if counts[num] > 0:
                    next_active.append(num)

            active = next_active

        return ans
