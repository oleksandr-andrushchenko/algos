# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))
