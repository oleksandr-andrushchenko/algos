# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other,
# otherwise return false.

class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        prev = -1

        for i, num in enumerate(nums):
            if num == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i

        return True
