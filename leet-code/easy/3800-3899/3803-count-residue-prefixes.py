# You are given a string s consisting only of lowercase English letters.
#
# A prefix of s is called a residue if the number of distinct characters in the prefix is equal to len(prefix) % 3.
#
# Return the count of residue prefixes in s.
#
# A prefix of a string is a non-empty substring that starts from the beginning of the string and extends to any point
# within it.

class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        count = 0

        for i, char in enumerate(s, 1):
            seen.add(char)

            if len(seen) == i % 3:
                count += 1

        return count
