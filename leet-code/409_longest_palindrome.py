# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        counts = Counter(s)
        length = 0
        odd_found = False

        for c in counts.values():
            # use all even counts, and the largest even part of odd counts
            length += (c // 2) * 2
            if c % 2 == 1:
                odd_found = True

        # if any character had an odd count, we can place one in the center
        if odd_found:
            length += 1

        return length