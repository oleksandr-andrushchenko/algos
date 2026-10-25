# You are given a positive integer n.
#
# Return the integer obtained by removing all zeros from the decimal representation of n.


class Solution:
    def removeZeros(self, n: int) -> int:
        return int(str(n).replace('0', ''))
