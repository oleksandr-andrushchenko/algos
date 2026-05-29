# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
#
# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d

class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)

        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1

        return count
