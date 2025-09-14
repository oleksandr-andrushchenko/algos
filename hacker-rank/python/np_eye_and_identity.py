# Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

# Input Format
#
# A single line containing the space separated values of  and .
#  denotes the rows.
#  denotes the columns.

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())

    np.set_printoptions(legacy="1.13")

    if n == m:
        res = np.identity(n)
    else:
        res = np.eye(n, m, k=0)

    print(res)
