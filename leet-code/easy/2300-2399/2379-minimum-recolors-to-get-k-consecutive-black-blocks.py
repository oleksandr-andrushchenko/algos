# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of
# the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
#
# You are also given an integer k, which is the desired number of consecutive black blocks.
#
# In one operation, you can recolor a white block such that it becomes a black block.
#
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = blocks[:k].count('W')
        minimum = white_count

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                white_count += 1

            if blocks[i - k] == 'W':
                white_count -= 1

            minimum = min(minimum, white_count)

        return minimum
