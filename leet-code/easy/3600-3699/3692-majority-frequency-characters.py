# You are given a string s consisting of lowercase English letters.
#
# The frequency group for a value k is the set of characters that appear exactly k times in s.
#
# The majority frequency group is the frequency group that contains the largest number of distinct characters.
#
# Return a string containing all characters in the majority frequency group, in any order. If two or more frequency
# groups tie for that largest size, pick the group whose frequency k is larger.


from collections import Counter, defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counts = Counter(s)
        groups = defaultdict(list)

        for char, freq in counts.items():
            groups[freq].append(char)

        best_freq = max(groups, key=lambda freq: (len(groups[freq]), freq))

        return ''.join(groups[best_freq])
