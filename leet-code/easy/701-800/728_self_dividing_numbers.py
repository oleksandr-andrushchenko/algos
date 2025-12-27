# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []

        for num in range(left, right + 1):
            temp = num
            is_self_dividing = True

            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break
                temp //= 10

            if is_self_dividing:
                result.append(num)

        return result
