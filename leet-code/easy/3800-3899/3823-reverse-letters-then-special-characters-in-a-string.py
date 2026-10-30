# You are given a string s consisting of lowercase English letters and special characters.
#
# Your task is to perform these in order:
#
# Reverse the lowercase letters and place them back into the positions originally occupied by letters.
# Reverse the special characters and place them back into the positions originally occupied by special characters.
# Return the resulting string after performing the reversals.

class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [c for c in s if 'a' <= c <= 'z']
        special = [c for c in s if not 'a' <= c <= 'z']

        return ''.join(
            letters.pop() if 'a' <= c <= 'z' else special.pop()
            for c in s
        )
