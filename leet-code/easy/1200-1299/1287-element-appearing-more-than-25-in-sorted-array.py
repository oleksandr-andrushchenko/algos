# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more
# than 25% of the time, return that integer.

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)

        # Check quarter positions
        for i in [0, n // 4, n // 2, 3 * n // 4]:
            candidate = arr[i]

            # Count occurrences using binary search boundaries
            left = self.first_occurrence(arr, candidate)
            right = self.last_occurrence(arr, candidate)

            if right - left + 1 > n // 4:
                return candidate

    def first_occurrence(self, arr, target):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def last_occurrence(self, arr, target):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi
