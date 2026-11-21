# You are given an integer array nums.
#
# An integer x is special if all occurrences of x in nums appear in a single contiguous block.
#
# Return the number of distinct special integers in nums.

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        blocks = {}

        for i, num in enumerate(nums):
            if i == 0 or num != nums[i - 1]:
                blocks[num] = blocks.get(num, 0) + 1

        return sum(count == 1 for count in blocks.values())
