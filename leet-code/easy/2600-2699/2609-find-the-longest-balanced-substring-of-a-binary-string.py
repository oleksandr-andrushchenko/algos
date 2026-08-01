# You are given a binary string s consisting only of zeroes and ones.
#
# A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number
# of ones inside the substring. Notice that the empty substring is considered a balanced substring.
#
# Return the length of the longest balanced substring of s.
#
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = ones = 0
        answer = 0

        for char in s:
            if char == "0":
                if ones > 0:
                    zeros = 0
                    ones = 0
                zeros += 1
            else:
                ones += 1
                answer = max(answer, 2 * min(zeros, ones))

        return answer
