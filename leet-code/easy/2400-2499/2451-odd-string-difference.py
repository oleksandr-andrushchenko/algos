# You are given an array of equal-length strings words. Assume that the length of each string is n.
#
# Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where
# difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is
# the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.
#
# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one. You should find that string.
#
# Return the string in words that has different difference integer array.

from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_difference(word: str) -> tuple[int, ...]:
            return tuple(
                ord(word[i + 1]) - ord(word[i])
                for i in range(len(word) - 1)
            )

        first = get_difference(words[0])
        second = get_difference(words[1])

        # If the first two patterns match, the odd string is later.
        if first == second:
            for word in words[2:]:
                if get_difference(word) != first:
                    return word

        # Otherwise, compare with the third word to determine
        # whether the first or second string is the odd one.
        third = get_difference(words[2])

        return words[0] if first != third else words[1]
