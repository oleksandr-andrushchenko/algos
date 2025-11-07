# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res < 0:
                right = mid - 1
            else:
                left = mid + 1
