# Given an array of integers nums and an integer k, an element nums[i] is considered good if it is strictly greater than
# the elements at indices i - k and i + k (if those indices exist). If neither of these indices exists, nums[i] is still considered good.
#
# Return the sum of all the good elements in the array.


from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0

        for i, num in enumerate(nums):
            if (
                    (i < k or num > nums[i - k])
                    and (i + k >= n or num > nums[i + k])
            ):
                total += num

        return total
