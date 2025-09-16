# Task
#
# There is a collection of input strings and a collection of query strings.
# For each query string, determine how many times it occurs in the list of input strings.
# Return an array of the results.

# Input Format
#
# The first line contains and integer , the size of .
# Each of the next  lines contains a string .
# The next line contains , the size of .
# Each of the next  lines contains a string .

# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries

from collections import Counter


def matchingStrings(stringList, queries):
    freq = Counter(stringList)
    return [freq[q] for q in queries]


if __name__ == '__main__':
    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    print('\n'.join(map(str, res)))
