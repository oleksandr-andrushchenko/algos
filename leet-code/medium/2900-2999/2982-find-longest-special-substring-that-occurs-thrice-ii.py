# You are given a string s that consists of lowercase English letters.
#
# A string is called special if it is made up of only a single character. For example, the string "abc" is not special,
# whereas the strings "ddd", "zz", and "f" are special.
#
# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring
# occurs at least thrice.
#
# A substring is a contiguous non-empty sequence of characters within a string.

class Solution:
    def maximumLength(self, s: str) -> int:
        def can_make(length: int) -> bool:
            counts = [0] * 26
            i = 0

            while i < len(s):
                j = i

                while j < len(s) and s[j] == s[i]:
                    j += 1

                run_length = j - i

                if run_length >= length:
                    index = ord(s[i]) - ord('a')
                    counts[index] += run_length - length + 1

                    if counts[index] >= 3:
                        return True

                i = j

            return False

        left, right = 1, len(s)
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can_make(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
