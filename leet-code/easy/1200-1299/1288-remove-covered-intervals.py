# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are
# covered by another interval in the list.
#
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
#
# Return the number of remaining intervals.

class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by left ascending, right descending
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_right = 0

        for left, right in intervals:
            if right > max_right:
                count += 1
                max_right = right
            # else: covered, skip

        return count
