# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
#
# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j]
# where |arr1[i]-arr2[j]| <= d.

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                count += 1

        return count
