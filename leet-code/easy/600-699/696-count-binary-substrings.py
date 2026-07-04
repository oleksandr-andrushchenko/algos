# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_run = 0
        curr_run = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run += 1
            else:
                count += min(prev_run, curr_run)
                prev_run = curr_run
                curr_run = 1

        count += min(prev_run, curr_run)
        return count
