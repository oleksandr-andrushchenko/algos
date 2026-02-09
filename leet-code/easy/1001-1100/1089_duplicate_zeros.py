# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input
# array in place and do not return anything.

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)

        i = n - 1
        j = n + zeros - 1  # virtual extended index

        while i < j:
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            i -= 1
            j -= 1
