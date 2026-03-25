# You are given a string s.
#
# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is
# equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.
#
# Return the number of good splits you can make in s.

class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)

        left_distinct = [0] * n
        right_distinct = [0] * n

        seen = set()
        for i in range(n):
            seen.add(s[i])
            left_distinct[i] = len(seen)

        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            right_distinct[i] = len(seen)

        result = 0
        for i in range(n - 1):
            if left_distinct[i] == right_distinct[i + 1]:
                result += 1

        return result
