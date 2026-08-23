# You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum number of
# right shifts required to sort nums and -1 if this is not possible.
#
# A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                # There can be only one "break"
                if nums[-1] > nums[0]:
                    return -1

                # Everything after the break must be sorted
                for j in range(i + 1, n - 1):
                    if nums[j] > nums[j + 1]:
                        return -1

                return n - i - 1

        return 0
