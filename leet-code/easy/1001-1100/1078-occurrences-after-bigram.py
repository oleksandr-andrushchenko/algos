# Given two strings first and second, consider occurrences in some text of the form "first second third", where second
# comes immediately after first, and third comes immediately after second.
#
# Return an array of all the words third for each occurrence of "first second third".

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        result = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])

        return result
