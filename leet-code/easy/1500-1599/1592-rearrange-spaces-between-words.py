# You are given a string text of words that are placed among some number of spaces. Each word consists of one or more
# lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.
#
# Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number
# is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the
# returned string should be the same length as text.
#
# Return the string after rearranging the spaces.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(' ')
        words = text.split()
        n = len(words)

        if n == 1:
            return words[0] + ' ' * total_spaces

        spaces_between = total_spaces // (n - 1)
        extra_spaces = total_spaces % (n - 1)

        space_str = ' ' * spaces_between
        result = space_str.join(words)

        result += ' ' * extra_spaces

        return result
