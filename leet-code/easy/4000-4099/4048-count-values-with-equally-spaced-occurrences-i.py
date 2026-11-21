# You are given an integer array nums.
#
# An integer x is called special if:
#
# x appears exactly three times in nums.
# All three occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at indices
# i1 < i2 < i3, then i2 - i1 = i3 - i2.
# Return the number of distinct special integers in nums.

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        positions = {}

        for i, num in enumerate(nums):
            positions.setdefault(num, []).append(i)

        return sum(
            len(indices) == 3
            and indices[1] - indices[0] == indices[2] - indices[1]
            for indices in positions.values()
        )
