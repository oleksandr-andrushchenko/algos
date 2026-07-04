# Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into
# lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify
# the non '?' characters.
#
# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
#
# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution,
# return any of them. It can be shown that an answer is always possible with the given constraints.

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                for ch in 'abc':  # only 3 letters are enough
                    prev = s[i - 1] if i > 0 else ''
                    nxt = s[i + 1] if i < n - 1 else ''

                    if ch != prev and ch != nxt:
                        s[i] = ch
                        break

        return ''.join(s)
