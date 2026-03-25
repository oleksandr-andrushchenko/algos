# Given an array of integers arr, return the number of subarrays with an odd sum.
#
# Since the answer can be very large, return it modulo 109 + 7.

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7

        even_count = 1  # empty prefix
        odd_count = 0

        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1

        return result % MOD
