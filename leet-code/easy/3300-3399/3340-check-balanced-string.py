# You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits
# at even indices is equal to the sum of digits at odd indices.
#
# Return true if num is balanced, otherwise return false.

class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = sum(int(num[i]) for i in range(0, len(num), 2))
        odd_sum = sum(int(num[i]) for i in range(1, len(num), 2))

        return even_sum == odd_sum
