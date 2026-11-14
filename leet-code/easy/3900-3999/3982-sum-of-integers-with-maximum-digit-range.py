# You are given an integer array nums.
#
# The digit range of an integer is defined as the difference between its largest digit and smallest digit.
#
# For example, the digit range of 5724 is 7 - 2 = 5.
#
# Return the sum of all integers in nums whose digit range is equal to the maximum digit range among all integers in the
# array.

class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        best_range = -1
        total = 0

        for num in nums:
            digits = str(abs(num))
            digit_range = int(max(digits)) - int(min(digits))

            if digit_range > best_range:
                best_range = digit_range
                total = num
            elif digit_range == best_range:
                total += num

        return total
