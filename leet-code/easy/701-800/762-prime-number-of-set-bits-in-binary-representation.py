# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime
# number of set bits in their binary representation.
#
# Recall that the number of set bits an integer has is the number of 1's present when written in binary.
#
# For example, 21 written in binary is 10101, which has 3 set bits.

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Prime numbers up to 20 (max possible set bits)
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}

        count = 0
        for num in range(left, right + 1):
            # Count set bits using Python built-in
            set_bits = bin(num).count("1")

            if set_bits in prime_set:
                count += 1

        return count
