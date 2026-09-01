# You are given three strings: s1, s2, and s3. In one operation you can choose one of these strings and delete its
# rightmost character. Note that you cannot completely empty a string.
#
# Return the minimum number of operations required to make the strings equal. If it is impossible to make them equal,
# return -1.

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        common = 0

        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                common += 1
            else:
                break

        if common == 0:
            return -1

        return len(s1) + len(s2) + len(s3) - 3 * common
