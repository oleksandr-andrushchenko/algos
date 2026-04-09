# Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest
# 5% of the elements.
#
# Answers within 10-5 of the actual answer will be considered accepted.

class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        n = len(arr)
        k = n // 20  # 5% from each side

        trimmed = arr[k:n - k]
        return sum(trimmed) / len(trimmed)
