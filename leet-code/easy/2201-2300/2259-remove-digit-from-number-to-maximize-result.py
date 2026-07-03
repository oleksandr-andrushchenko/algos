# You are given a string number representing a positive integer and a character digit.
#
# Return the resulting string after removing exactly one occurrence of digit from number such that the value of the
# resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in
# number.

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""

        for i in range(len(number)):
            if number[i] == digit:
                candidate = number[:i] + number[i + 1:]

                if candidate > best:
                    best = candidate

        return best
