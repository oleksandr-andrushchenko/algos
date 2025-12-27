# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
#
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist,
# return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters)

        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left % len(letters)]
