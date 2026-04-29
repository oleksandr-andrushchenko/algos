# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the
# array.
#
# Return the sum of all the unique elements of nums.

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        return sum(num for num, freq in counts.items() if freq == 1)
