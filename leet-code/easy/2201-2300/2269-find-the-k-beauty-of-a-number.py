# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the
# following conditions:
#
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
#
# Note:
#
# Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0

        for i in range(len(s) - k + 1):
            value = int(s[i:i + k])

            if value != 0 and num % value == 0:
                count += 1

        return count
