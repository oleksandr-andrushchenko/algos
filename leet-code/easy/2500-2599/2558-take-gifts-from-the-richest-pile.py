# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
#
# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.
# Return the number of gifts remaining after k seconds.

import heapq
from math import isqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            heapq.heappush(heap, -isqrt(largest))

        return -sum(heap)
