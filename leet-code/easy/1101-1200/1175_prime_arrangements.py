# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
#
# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two
# positive integers both smaller than it.)
#
# Since the answer may be large, return the answer modulo 10^9 + 7.

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # Count primes up to n using simple sieve
        def count_primes(n):
            if n < 2:
                return 0
            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False

            for i in range(2, int(n ** 0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, n + 1, i):
                        sieve[j] = False

            return sum(sieve)

        p = count_primes(n)

        # Compute factorial mod
        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % MOD
            return result

        return (factorial(p) * factorial(n - p)) % MOD
