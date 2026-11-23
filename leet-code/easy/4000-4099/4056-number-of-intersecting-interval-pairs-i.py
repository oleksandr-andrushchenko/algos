# You are given a 2D integer array intervals of n elements, where intervals[i] = [starti, endi] represents the closed
# interval from starti to endi.
#
# Return the number of pairs of indices (i, j) such that 0 <= i < j < n and intervals[i] and intervals[j] intersect.
#
# Two intervals intersect if they have at least one point in common, including when they only share an endpoint.

import heapq


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        active_ends = []
        count = 0

        for start, end in sorted(intervals):
            while active_ends and active_ends[0] < start:
                heapq.heappop(active_ends)

            count += len(active_ends)
            heapq.heappush(active_ends, end)

        return count
