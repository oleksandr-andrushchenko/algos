# You are given an array of n strings strs, all of the same length.
#
# The strings can be arranged such that there is one on each line, making a grid.
#
# For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed),
# columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
#
# Return the number of columns that you will delete.

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        if not strs:
            return 0

        n_cols = len(strs[0])
        n_rows = len(strs)
        delete_count = 0

        for col in range(n_cols):
            for row in range(1, n_rows):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break  # no need to check further in this column

        return delete_count
