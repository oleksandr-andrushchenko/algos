# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
# and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        word = []

        for ch in s:
            if ch.isspace():
                # flush word
                if word:
                    result.append(''.join(reversed(word)))
                    word = []
                result.append(ch)
            else:
                word.append(ch)

        # flush last word
        if word:
            result.append(''.join(reversed(word)))

        return ''.join(result)
