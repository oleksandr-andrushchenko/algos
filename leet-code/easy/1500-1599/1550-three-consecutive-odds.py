# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return
# false.

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0

        for num in arr:
            if num % 2 == 1:  # odd number
                count += 1
                if count == 3:
                    return True
            else:
                count = 0  # reset if even

        return False