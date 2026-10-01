# You are given an array nums of n integers and two integers k and x.
#
# The x-sum of an array is calculated by the following procedure:
#
# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences,
# the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
#
# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []

        for i in range(len(nums) - k + 1):
            count = Counter(nums[i:i + k])

            top = sorted(
                count.items(),
                key=lambda item: (item[1], item[0]),
                reverse=True
            )[:x]

            result.append(
                sum(value * frequency for value, frequency in top)
            )

        return result
