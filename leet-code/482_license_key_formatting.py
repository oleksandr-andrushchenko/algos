# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.
#
# We want to reformat the string s such that each group contains exactly k characters, except for the first group,
# which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash
# inserted between two groups, and you should convert all lowercase letters to uppercase.
#
# Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove all dashes and convert to uppercase
        clean = s.replace("-", "").upper()

        # Build the result from the end
        res = []
        while len(clean) > k:
            res.append(clean[-k:])
            clean = clean[:-k]

        # Add the remaining first group (can be shorter)
        if clean:
            res.append(clean)

        # Reverse because we built it from the end
        res.reverse()
        return "-".join(res)
