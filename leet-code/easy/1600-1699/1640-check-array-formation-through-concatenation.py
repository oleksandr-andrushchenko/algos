# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces
# are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not
# allowed to reorder the integers in each array pieces[i].
#
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        # Map first element -> piece
        first_map = {p[0]: p for p in pieces}

        i = 0
        while i < len(arr):
            if arr[i] not in first_map:
                return False

            piece = first_map[arr[i]]

            # Check if piece matches arr starting at i
            for num in piece:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1

        return True
