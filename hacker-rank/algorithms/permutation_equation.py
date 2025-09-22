# Given a sequence of  integers,  where each element is distinct and satisfies .
# For each  where , that is  increments from  to , find any integer  such that  and keep a history of the values of  in a return array.

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Map value to position (1-indexed)
    pos = {val: i + 1 for i, val in enumerate(p)}
    result = []
    for x in range(1, len(p) + 1):
        k = pos[x]  # p[k] = x
        y = pos[k]  # p[y] = k
        result.append(y)
    return result


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
