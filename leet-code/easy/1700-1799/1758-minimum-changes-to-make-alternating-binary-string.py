# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1'
# or vice versa.
#
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating,
# while the string "0100" is not.
#
# Return the minimum number of operations needed to make s alternating.

class Solution:
    def minOperations(self, s: str) -> int:
        changes_start_0 = 0  # pattern: 0101...
        changes_start_1 = 0  # pattern: 1010...

        for i, ch in enumerate(s):
            expected_0 = '0' if i % 2 == 0 else '1'
            expected_1 = '1' if i % 2 == 0 else '0'

            if ch != expected_0:
                changes_start_0 += 1
            if ch != expected_1:
                changes_start_1 += 1

        return min(changes_start_0, changes_start_1)
