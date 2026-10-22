# You are given an integer array nums and an integer k.
#
# Return an integer denoting the sum of all elements in nums whose frequency is divisible by k, or 0 if there are no
# such elements.
#
# Note: An element is included in the sum exactly as many times as it appears in the array if its total frequency is
# divisible by k.


from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)

        return sum(
            num * freq
            for num, freq in counts.items()
            if freq % k == 0
        )
