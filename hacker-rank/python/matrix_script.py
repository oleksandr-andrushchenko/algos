# Task
#
# Neo has a complex matrix script. The matrix script is a  X  grid of strings.
# It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
# Neo reads the column from top to bottom and starts reading from the leftmost column.
#
# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
#
# Neo feels that there is no need to use 'if' conditions for decoding.
#
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

# Input Format
#
# The first line contains space-separated integers  (rows) and  (columns) respectively.
# The next  lines contain the row elements of the matrix script.

# Output Format
#
# Print the decoded matrix script.

import re

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]

    decoded = ''.join(matrix[j][i] for i in range(m) for j in range(n))

    cleaned = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded)
    print(cleaned)
