# You are given an array of positive integers nums.
#
# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
#
# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

from math import gcd, lcm
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            product = 1
            g = 0
            l = 1

            for j in range(i, len(nums)):
                product *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if product == g * l:
                    result = max(result, j - i + 1)

        return result
