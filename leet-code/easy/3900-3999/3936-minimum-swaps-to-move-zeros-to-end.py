# You are given an integer array nums.
#
# In one operation, you can choose any two distinct indices i and j and swap nums[i] and nums[j].
#
# Return an integer denoting the minimum number of operations required to move all 0s to the end of the array.

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        nonzero_count = len(nums) - nums.count(0)
        return sum(nums[i] == 0 for i in range(nonzero_count))
