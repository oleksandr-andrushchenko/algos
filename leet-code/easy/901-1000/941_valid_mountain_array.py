# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Walk up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # Walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # Valid if we reach the end
        return i == n - 1
