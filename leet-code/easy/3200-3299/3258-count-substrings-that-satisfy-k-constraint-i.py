# You are given a binary string s and an integer k.
#
# A binary string satisfies the k-constraint if either of the following conditions holds:
#
# The number of 0's in the string is at most k.
# The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings of s that satisfy the k-constraint.

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        zeros = 0
        ones = 0
        result = 0

        for right in range(len(s)):
            if s[right] == "0":
                zeros += 1
            else:
                ones += 1

            while zeros > k and ones > k:
                if s[left] == "0":
                    zeros -= 1
                else:
                    ones -= 1
                left += 1

            result += right - left + 1

        return result
