# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 == 1:
            return False

        close_to_open_tags = {")": "(", "]": "[", "}": "{"}

        opens = []
        for char in s:
            if char in close_to_open_tags:  # close tag
                if not opens:
                    return False

                open_tag = close_to_open_tags[char]
                expected_open_tag = opens.pop()

                if open_tag != expected_open_tag:
                    return False
            else:
                opens.append(char)  # open tag

        return len(opens) == 0
