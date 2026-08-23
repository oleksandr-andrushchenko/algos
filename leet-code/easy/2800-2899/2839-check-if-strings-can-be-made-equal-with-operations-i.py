# You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.
#
# You can apply the following operation on any of the two strings any number of times:
#
# Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
                sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]])
                and sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
        )
