# In a string s of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
#
# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of
# the group. In the above example, "xxxx" has the interval [3,6].
#
# A group is considered large if it has 3 or more characters.
#
# Return the intervals of every large group sorted in increasing order by start index.

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []
        n = len(s)

        start = 0
        for i in range(n):
            # end of group (next char different or end of string)
            if i == n - 1 or s[i] != s[i + 1]:
                if i - start + 1 >= 3:
                    res.append([start, i])
                start = i + 1

        return res
