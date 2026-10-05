# You are given a 2D array events which represents a sequence of events where a child pushes a series of buttons on a
# keyboard.
#
# Each events[i] = [indexi, timei] indicates that the button at index indexi was pressed at time timei.
#
# The array is sorted in increasing order of time.
# The time taken to press a button is the difference in time between consecutive button presses. The time for the first
# button is simply the time at which it was pressed.
# Return the index of the button that took the longest time to push. If multiple buttons have the same longest time,
# return the button with the smallest index.

from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        result = events[0][0]
        longest = events[0][1]

        for i in range(1, len(events)):
            index, time = events[i]
            duration = time - events[i - 1][1]

            if duration > longest or (duration == longest and index < result):
                longest = duration
                result = index

        return result
