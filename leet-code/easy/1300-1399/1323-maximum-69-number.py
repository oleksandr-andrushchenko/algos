# You are given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = list(str(num))

        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break

        return int(''.join(num_str))
