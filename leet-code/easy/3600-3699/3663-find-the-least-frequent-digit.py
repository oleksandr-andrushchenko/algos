# Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have
# the same frequency, choose the smallest digit.
#
# Return the chosen digit as an integer.
#
# The frequency of a digit x is the number of times it appears in the decimal representation of n.


from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counts = Counter(map(int, str(n)))
        return min(counts, key=lambda digit: (counts[digit], digit))
