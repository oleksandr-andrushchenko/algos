# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings
# (i.e. left substring and right substring).
#
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right
# substring.

class Solution:
    def maxScore(self, s: str) -> int:
        ones_right = s.count('1')
        zeros_left = 0
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1

            max_score = max(max_score, zeros_left + ones_right)

        return max_score
