# Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.
#
# A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times
# consecutively without overlapping. A pattern is defined by its length and the number of repetitions.
#
# Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.

class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n - m * k + 1):
            pattern = arr[i:i + m]
            valid = True

            for j in range(1, k):
                if arr[i + j * m: i + (j + 1) * m] != pattern:
                    valid = False
                    break

            if valid:
                return True

        return False
