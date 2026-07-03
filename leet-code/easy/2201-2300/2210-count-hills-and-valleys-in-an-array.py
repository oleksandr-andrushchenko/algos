# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors
# of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of
# i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
#
# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right
# of the index.
#
# Return the number of hills and valleys in nums.

from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove adjacent duplicates because equal neighbors are part of the same hill/valley
        arr = [nums[0]]

        for num in nums[1:]:
            if num != arr[-1]:
                arr.append(num)

        count = 0

        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                count += 1
            elif arr[i - 1] > arr[i] < arr[i + 1]:
                count += 1

        return count
