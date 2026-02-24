# You are given an integer array deck where deck[i] represents the number written on the ith card.
#
# Partition the cards into one or more groups such that:
#
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        counts = Counter(deck).values()
        return reduce(gcd, counts) >= 2
