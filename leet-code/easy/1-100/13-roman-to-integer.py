# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        char_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        int_num = 0

        # XX + V + II

        while len(s):
            if (len(s) > 1) and (s[0] + s[1]) in char_map:
                int_num += char_map[s[0] + s[1]]
                s = s[2:]
            elif s[0] in char_map:
                int_num += char_map[s[0]]
                s = s[1:]

        return int_num
