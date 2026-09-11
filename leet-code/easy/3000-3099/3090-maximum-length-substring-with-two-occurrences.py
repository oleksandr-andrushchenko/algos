# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each
# character.

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        ans = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1

            while count[char] > 2:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
