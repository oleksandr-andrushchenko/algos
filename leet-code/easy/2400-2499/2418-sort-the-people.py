# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays
# are of length n.
#
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
#
# Return names sorted in descending order by the people's heights.

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = sorted(zip(heights, names), reverse=True)
        return [name for _, name in people]
