# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest
# contiguous segment of 0's in s, or return false otherwise.
#
# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment
# of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same
# applies if there is no 1's.

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = 0
        max_zeros = 0

        current_char = ""
        current_count = 0

        for char in s:
            if char == current_char:
                current_count += 1
            else:
                current_char = char
                current_count = 1

            if char == "1":
                max_ones = max(max_ones, current_count)
            else:
                max_zeros = max(max_zeros, current_count)

        return max_ones > max_zeros
