# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i + 1 < j with
# (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        current = 0
        parts = 0

        for i in range(len(arr) - 1):  # leave room for third part
            current += arr[i]
            if current == target:
                parts += 1
                current = 0
                if parts == 2:
                    return True

        return False
