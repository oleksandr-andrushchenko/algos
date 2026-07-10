# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the
# following properties:
#
# items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
# The value of each item in items is unique.
# Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items
# with value valuei.
#
# Note: ret should be returned in ascending order by value.

from typing import List
from collections import defaultdict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weights = defaultdict(int)

        for value, weight in items1:
            weights[value] += weight

        for value, weight in items2:
            weights[value] += weight

        return sorted(weights.items())
