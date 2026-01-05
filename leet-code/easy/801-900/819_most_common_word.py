# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not
# banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
#
# Note that words can not contain punctuation symbols.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)

        normalized = []
        for ch in paragraph.lower():
            if ch.isalpha():
                normalized.append(ch)
            else:
                normalized.append(" ")

        words = "".join(normalized).split()

        freq = {}
        for word in words:
            if word not in banned_set:
                freq[word] = freq.get(word, 0) + 1

        return max(freq, key=freq.get)
