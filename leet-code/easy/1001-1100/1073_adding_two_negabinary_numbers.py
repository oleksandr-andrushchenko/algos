# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.
#
# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.
# For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.
# A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.
#
# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            a = arr1[i] if i >= 0 else 0
            b = arr2[j] if j >= 0 else 0

            total = a + b + carry

            result.append(total & 1)  # same as total % 2

            carry = -(total >> 1)  # same as -(total // 2)

            i -= 1
            j -= 1

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]
