# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
