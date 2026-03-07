# You are given a string s. Reorder the string using the following algorithm:
#
# Remove the smallest character from s and append it to the result.
# Remove the smallest character from s that is greater than the last appended character, and append it to the result.
# Repeat step 2 until no more characters can be removed.
# Remove the largest character from s and append it to the result.
# Remove the largest character from s that is smaller than the last appended character, and append it to the result.
# Repeat step 5 until no more characters can be removed.
# Repeat steps 1 through 6 until all characters from s have been removed.
# If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.
#
# Return the resulting string after reordering s using this algorithm.

from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        result = []

        while len(result) < len(s):
            # increasing
            for c in range(ord('a'), ord('z') + 1):
                ch = chr(c)
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1

            # decreasing
            for c in range(ord('z'), ord('a') - 1, -1):
                ch = chr(c)
                if count[ch] > 0:
                    result.append(ch)
                    count[ch] -= 1

        return ''.join(result)