# Task
#
# There is a horizontal row of  cubes. The length of each cube is given.
# You need to create a new vertical pile of cubes.
# The new pile should follow these directions: if  is on top of  then .
#
# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
# Print Yes if it is possible to stack the cubes. Otherwise, print No.

# Input Format
#
# The first line contains a single integer , the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains , the number of cubes.
# The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

# Output Format
#
# For each test case, output a single line containing either Yes or No.

from collections import deque

if __name__ == "__main__":
    n = int(input())

    results = []
    for _ in range(n):
        m = int(input())
        blocks = deque(map(int, input().split()[:m]))
        if not blocks:
            continue

        result = True

        last = blocks.pop() if blocks[-1] > blocks[0] else blocks.popleft()

        while len(blocks) > 0:
            if max(blocks[0], blocks[-1]) > last:
                result = False
                break
            last = blocks.pop() if blocks[-1] > blocks[0] else blocks.popleft()
        results.append(result)

    [print("Yes" if yes else "No") for yes in results]
