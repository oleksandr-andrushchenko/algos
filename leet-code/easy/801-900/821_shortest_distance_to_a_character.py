# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
# and answer[i] is the distance from index i to the closest occurrence of character c in s.
#
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [float('inf')] * n

        # Left to right
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # Right to left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer
