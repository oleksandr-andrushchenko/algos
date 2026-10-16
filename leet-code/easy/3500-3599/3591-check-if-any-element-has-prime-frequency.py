# You are given an integer array nums.
#
# Return true if the frequency of any element of the array is prime, otherwise, return false.
#
# The frequency of an element x is the number of times it occurs in the array.
#
# A prime number is a natural number greater than 1 with only two factors, 1 and itself.


from collections import Counter
from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        for freq in Counter(nums).values():
            if freq < 2:
                continue

            if all(freq % i != 0 for i in range(2, int(freq ** 0.5) + 1)):
                return True

        return False
