# You are given an integer array nums.
#
# Return an integer denoting the first even integer (earliest by array index) that appears exactly once in nums. If no
# such integer exists, return -1.
#
# An integer x is considered even if it is divisible by 2.


from collections import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counts = Counter(nums)

        for num in nums:
            if num % 2 == 0 and counts[num] == 1:
                return num

        return -1
