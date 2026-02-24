# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency
# of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first_index = {}
        last_index = {}
        count = {}

        for i, num in enumerate(nums):
            if num not in first_index:
                first_index[num] = i
            last_index[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        min_length = float('inf')

        for num in count:
            if count[num] == degree:
                length = last_index[num] - first_index[num] + 1
                min_length = min(min_length, length)

        return min_length
