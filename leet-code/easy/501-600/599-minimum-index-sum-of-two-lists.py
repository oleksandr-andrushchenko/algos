# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
#
# A common string is a string that appeared in both list1 and list2.
#
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j]
# then i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum. Return the answer in any order.

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_map = {s: i for i, s in enumerate(list1)}

        best = float('inf')
        result = []

        for j, s in enumerate(list2):
            if s in index_map:
                total = j + index_map[s]
                if total < best:
                    best = total
                    result = [s]
                elif total == best:
                    result.append(s)

        return result
