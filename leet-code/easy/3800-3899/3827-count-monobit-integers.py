# You are given an integer n.
#
# An integer is called Monobit if all bits in its binary representation are the same.
#
# Return the count of Monobit integers in the range [0, n] (inclusive).

class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1  # Include 0
        num = 1

        while num <= n:
            count += 1
            num = (num << 1) | 1

        return count
