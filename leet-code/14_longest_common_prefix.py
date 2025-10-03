# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_str = min(strs, key=len)

        for pref_len, char in enumerate(min_str):
            for string in strs:
                if string[pref_len] != char:
                    return min_str[:pref_len]

        return min_str
