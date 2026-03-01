# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
#
# After doing so, return the array.

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_so_far = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, current)

        return arr
