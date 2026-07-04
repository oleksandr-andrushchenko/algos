# You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd
# digits or both even digits).
#
# Return the largest possible value of num after any number of swaps.

class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))

        even_digits = sorted([d for d in digits if int(d) % 2 == 0], reverse=True)
        odd_digits = sorted([d for d in digits if int(d) % 2 == 1], reverse=True)

        result = []

        for d in digits:
            if int(d) % 2 == 0:
                result.append(even_digits.pop(0))
            else:
                result.append(odd_digits.pop(0))

        return int("".join(result))
