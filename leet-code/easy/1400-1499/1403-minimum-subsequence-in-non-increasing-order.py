# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the
# non included elements in such subsequence.
#
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions,
# return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
#
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in
# non-increasing order.

class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)

        total = sum(nums)
        curr = 0
        result = []

        for n in nums:
            curr += n
            result.append(n)
            if curr > total - curr:
                break

        return result
