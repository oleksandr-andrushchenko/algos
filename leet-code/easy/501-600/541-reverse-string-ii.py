# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start
# of the string.
#
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal
# to k characters, then reverse the first k characters and leave the other as original.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)

        for i in range(0, n, 2 * k):
            # Reverse the first k chars in each 2k block
            chars[i:i + k] = reversed(chars[i:i + k])

        return ''.join(chars)
