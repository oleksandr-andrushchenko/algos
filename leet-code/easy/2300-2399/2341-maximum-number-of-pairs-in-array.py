# You are given a 0-indexed integer array nums. In one operation, you may do the following:
#
# Choose two integers in nums that are equal.
# Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
#
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1]
# is the number of leftover integers in nums after doing the operation as many times as possible.

from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        leftover = 0

        for count in Counter(nums).values():
            pairs += count // 2
            leftover += count % 2

        return [pairs, leftover]
