# You are given an integer n.
#
# We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong
# to the same group, whereas 13 and 3 belong to different groups.
#
# Return the number of groups that have the largest size, i.e. the maximum number of elements.

from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = sum(map(int, str(i)))
            groups[digit_sum] += 1

        max_size = max(groups.values())
        return sum(1 for v in groups.values() if v == max_size)
