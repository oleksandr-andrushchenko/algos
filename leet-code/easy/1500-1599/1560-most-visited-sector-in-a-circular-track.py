# Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1
# to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector
# rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]
#
# Return an array of the most visited sectors sorted in ascending order.
#
# Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the
# first example).

class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        start = rounds[0]
        end = rounds[-1]

        if start <= end:
            return list(range(start, end + 1))
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))
