# You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.
#
# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes.
# Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
# The final digits are then grouped as follows:
#
# 2 digits: A single block of length 2.
# 3 digits: A single block of length 3.
# 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1
# and produce at most two blocks of length 2.
#
# Return the phone number after formatting.

class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [c for c in number if c.isdigit()]
        res = []
        i = 0
        n = len(digits)

        while n - i > 4:
            res.append("".join(digits[i:i + 3]))
            i += 3

        # handle last 2, 3, or 4 digits
        remaining = n - i
        if remaining == 4:
            res.append("".join(digits[i:i + 2]))
            res.append("".join(digits[i + 2:i + 4]))
        else:
            res.append("".join(digits[i:]))

        return "-".join(res)
