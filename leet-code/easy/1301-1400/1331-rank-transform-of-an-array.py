# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Get sorted unique values
        sorted_unique = sorted(set(arr))

        # Step 2: Map each value to its rank
        rank = {num: i + 1 for i, num in enumerate(sorted_unique)}

        # Step 3: Replace values with ranks
        return [rank[num] for num in arr]
