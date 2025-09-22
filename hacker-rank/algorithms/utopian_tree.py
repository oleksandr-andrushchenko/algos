# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
# Each summer, its height increases by 1 meter.
#
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring.
# How tall will the tree be after  growth cycles?

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    height = 1
    for cycle in range(1, n + 1):
        if cycle % 2 == 1:
            height *= 2
        else:
            height += 1
    return height


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
