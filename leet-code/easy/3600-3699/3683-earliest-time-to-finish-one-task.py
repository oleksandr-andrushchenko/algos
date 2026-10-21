# You are given a 2D integer array tasks where tasks[i] = [si, ti].
#
# Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.
#
# Return the earliest time at which at least one task is finished.


from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(s + t for s, t in tasks)
