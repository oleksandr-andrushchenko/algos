# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        i = 0  # pointer for children
        j = 0  # pointer for cookies

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # cookie j satisfies child i
                i += 1
            # whether satisfied or not, move to next cookie
            j += 1

        return i
