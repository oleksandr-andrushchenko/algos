# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also
# given an integer k.
#
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k
# scores is minimized.
#
# Return the minimum possible difference.

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        answer = float('inf')

        for i in range(len(nums) - k + 1):
            answer = min(answer, nums[i + k - 1] - nums[i])

        return answer
