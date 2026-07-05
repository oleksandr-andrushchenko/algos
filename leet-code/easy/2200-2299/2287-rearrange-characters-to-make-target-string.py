# You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new
# strings.
#
# Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.

from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count = Counter(s)
        target_count = Counter(target)

        answer = float("inf")

        for char in target_count:
            answer = min(answer, s_count[char] // target_count[char])

        return answer
