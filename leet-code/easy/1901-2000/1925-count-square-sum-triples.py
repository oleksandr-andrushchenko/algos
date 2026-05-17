# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_square = a * a + b * b
                c = int(c_square ** 0.5)

                if c <= n and c * c == c_square:
                    count += 1

        return count
