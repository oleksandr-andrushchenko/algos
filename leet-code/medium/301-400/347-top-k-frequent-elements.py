# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        # heap of (-frequency, number)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
