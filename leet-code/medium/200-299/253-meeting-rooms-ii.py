# Given an array of meeting time intervals intervals where:
#
# intervals[i] = [start_i, end_i]
#
# Return the minimum number of conference rooms required so that all meetings can take place without overlapping in the
# same room.

import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        # min-heap of end times
        heap = []

        # add first meeting
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # if room is free (earliest ending meeting <= current start)
            if heap[0] <= start:
                heapq.heappop(heap)

            # assign current meeting to a room
            heapq.heappush(heap, end)

        return len(heap)
