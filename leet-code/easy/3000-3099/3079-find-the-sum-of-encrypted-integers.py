# You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x)
# replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.
#
# Return the sum of encrypted elements.

from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            s = str(num)
            max_digit = max(s)
            ans += int(max_digit * len(s))

        return ans
