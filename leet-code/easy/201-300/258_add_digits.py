# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            num_sum = sum(list(map(int, list(str(num)))))
            if num_sum < 10:
                return num_sum
            else:
                num = str(num_sum)



sol = Solution()
print(sol.addDigits(1090))