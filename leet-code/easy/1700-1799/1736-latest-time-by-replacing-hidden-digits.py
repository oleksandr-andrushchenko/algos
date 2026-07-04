# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).
#
# The valid times are those inclusively between 00:00 and 23:59.
#
# Return the latest valid time you can get from time by replacing the hidden digits.

class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)

        # Hour first digit
        if t[0] == '?':
            if t[1] == '?' or t[1] <= '3':
                t[0] = '2'
            else:
                t[0] = '1'

        # Hour second digit
        if t[1] == '?':
            if t[0] == '2':
                t[1] = '3'
            else:
                t[1] = '9'

        # Minute first digit
        if t[3] == '?':
            t[3] = '5'

        # Minute second digit
        if t[4] == '?':
            t[4] = '9'

        return ''.join(t)
