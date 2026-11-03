# You are given an integer n.
#
# Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
#
# In standard formatting:
#
# A comma is inserted after every three digits from the right.
# Numbers with fewer than 4 digits contain no commas.


class Solution:
    def countCommas(self, n: int) -> int:
        result = 0
        threshold = 1000

        while threshold <= n:
            result += n - threshold + 1
            threshold *= 1000

        return result
