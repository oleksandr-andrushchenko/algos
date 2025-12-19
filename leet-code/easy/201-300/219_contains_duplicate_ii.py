# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mapp = {}
        for i in range(len(nums)):
            if nums[i] in mapp and abs(mapp.get(nums[i]) - i) <= k:
                return True
            mapp[nums[i]] = i
        return False
