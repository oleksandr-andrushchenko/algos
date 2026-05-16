# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents
# an inclusive interval between starti and endi.
#
# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges.
# Return false otherwise.
#
# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

class Solution:
    def isCovered(
            self,
            ranges: list[list[int]],
            left: int,
            right: int
    ) -> bool:

        for num in range(left, right + 1):
            covered = False

            for start, end in ranges:
                if start <= num <= end:
                    covered = True
                    break

            if not covered:
                return False

        return True
