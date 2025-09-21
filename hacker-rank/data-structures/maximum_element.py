# You have an empty sequence, and you will be given  queries. Each query is one of these three types:
#
# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    st = []
    max_st = []
    result = []

    for op in operations:
        if op.startswith('1'):
            x = int(op.split()[1])
            st.append(x)
            if not max_st or x >= max_st[-1]:
                max_st.append(x)

        elif op == '2':
            if st:
                popped = st.pop()
                if popped == max_st[-1]:
                    max_st.pop()

        elif op == '3':
            if max_st:
                result.append(max_st[-1])

    return result


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
