# Given a string s of lower and upper case English letters.
#
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
#
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep
# doing this until the string becomes good.
#
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
#
# Notice that an empty string is also good.

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
