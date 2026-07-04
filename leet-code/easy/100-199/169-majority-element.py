# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


from typing import List
from collections import defaultdict


class Solution:
    def majorityElement2(self, nums: List[int]) -> int:
        target_cnt = len(nums) / 2
        cnt_map = defaultdict(int)

        for num in nums:
            cnt_map[num] += 1

            if cnt_map[num] > target_cnt:
                return num

    # Boyer–Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
