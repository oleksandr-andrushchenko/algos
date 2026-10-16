# You are given an integer n.
#
# Return the concatenation of the hexadecimal representation of n2 and the hexatrigesimal representation of n3.
#
# A hexadecimal number is defined as a base-16 numeral system that uses the digits 0 – 9 and the uppercase letters
# A - F to represent values from 0 to 15.
#
# A hexatrigesimal number is defined as a base-36 numeral system that uses the digits 0 – 9 and the uppercase letters
# A - Z to represent values from 0 to 35.


class Solution:
    def concatHex36(self, n: int) -> str:
        def convert(num: int, base: int) -> str:
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""

            while num:
                result = chars[num % base] + result
                num //= base

            return result or "0"

        return convert(n * n, 16) + convert(n * n * n, 36)
