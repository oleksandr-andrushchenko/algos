# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Create a max-heap by storing negative weights
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # Smash stones until 0 or 1 stone is left
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)  # heaviest
            second = -heapq.heappop(max_heap)  # second heaviest
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if max_heap else 0
