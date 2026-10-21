# You are given an integer array nums of length n.
#
# In one operation, choose any subarray nums[l...r] (0 <= l <= r < n) and replace each element in that subarray with the
# bitwise AND of all elements.
#
# Return the minimum number of operations required to make all elements of nums equal.
#
# A subarray is a contiguous non-empty sequence of elements within an array.


from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0 if len(set(nums)) == 1 else 1
