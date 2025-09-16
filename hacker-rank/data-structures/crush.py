# Task
#
# Starting with a 1-indexed array of zeros and a list of operations,
# for each operation add a value to each array element between two given indices, inclusive.
# Once all operations have been performed, return the maximum value in the array.

# Input Format
#
# The first line contains two space-separated integers  and , the size of the array and the number of queries.
# Each of the next  lines contains three space-separated integers ,  and , the left index, right index and number to add.

# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries

def arrayManipulation(n, queries):
    # Create difference array with an extra slot for boundary handling
    arr = [0] * (n + 2)

    # Mark start and end+1 for each operation
    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    # Compute prefix sum and track maximum value
    max_val = temp = 0
    for i in range(1, n + 1):
        temp += arr[i]
        max_val = max(max_val, temp)

    return max_val


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
