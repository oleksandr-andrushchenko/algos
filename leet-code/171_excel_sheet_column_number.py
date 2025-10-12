# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
