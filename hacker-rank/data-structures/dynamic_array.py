# Declare a 2-dimensional array, , with  empty arrays, all zero-indexed.
# Declare an integer, , and initialize it to 0.
# You need to process two types of queries:
#
# Query:
#
# Compute .
# Append the integer  to .
# Query:
#
# Compute .
# Set .
# Store the new value of  in an answers array.

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Initialize seqList with n empty lists
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        t, x, y = query
        # Compute index for the sequence
        idx = (x ^ lastAnswer) % n

        if t == 1:
            # Append y to the chosen sequence
            seqList[idx].append(y)
        elif t == 2:
            # Find the value and update lastAnswer
            size = len(seqList[idx])
            lastAnswer = seqList[idx][y % size]
            answers.append(lastAnswer)

    return answers


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
