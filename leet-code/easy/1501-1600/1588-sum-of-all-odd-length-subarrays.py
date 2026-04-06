# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
#
# A subarray is a contiguous subsequence of the array.

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0

        for i in range(n):
            left = i + 1
            right = n - i

            # total subarrays that include arr[i]
            total_subarrays = left * right

            # number of odd-length subarrays including arr[i]
            odd_count = (total_subarrays + 1) // 2

            total += arr[i] * odd_count

        return total