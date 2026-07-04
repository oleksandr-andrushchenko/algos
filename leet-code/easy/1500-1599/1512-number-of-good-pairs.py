# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        result = 0

        for num in nums:
            if num in count:
                result += count[num]
                count[num] += 1
            else:
                count[num] = 1

        return result