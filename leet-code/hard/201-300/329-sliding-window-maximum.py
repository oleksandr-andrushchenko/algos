# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
# the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
# by one position.
#
# Return the max sliding window.

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return []

        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):

            # remove elements out of window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # window is formed
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
