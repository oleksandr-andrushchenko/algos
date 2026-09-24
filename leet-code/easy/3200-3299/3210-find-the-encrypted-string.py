# You are given a string s and an integer k. Encrypt the string using the following algorithm:
#
# For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
# Return the encrypted string.

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)

        return "".join(
            s[(i + k) % n]
            for i in range(n)
        )
