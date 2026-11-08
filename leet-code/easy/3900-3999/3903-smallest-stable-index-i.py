# You are given an integer array nums of length n and an integer k.
#
# For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).
#
# In other words:
#
# max(nums[0..i]) is the largest value among the elements from index 0 to index i.
# min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
# An index i is called stable if its instability score is less than or equal to k.
#
# Return the smallest stable index. If no such index exists, return -1.

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if not nums:
            return -1

        candidate = 0
        prefix_max = candidate_max = nums[0]

        for i, value in enumerate(nums):
            prefix_max = max(prefix_max, value)

            if i == candidate:
                candidate_max = prefix_max

            if candidate_max - value > k:
                # Every index from candidate through i is unstable.
                candidate = i + 1

        return candidate if candidate < len(nums) else -1
