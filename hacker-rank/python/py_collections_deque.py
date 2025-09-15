# Task
#
# Perform append, pop, popleft and appendleft methods on an empty deque .

# Input Format
#
# The first line contains an integer , the number of operations.
# The next  lines contains the space separated names of methods and their values.

# Output Format
#
# Print the space separated elements of deque .

from collections import deque

if __name__ == "__main__":
    n = int(input())
    q = deque()

    for _ in range(n):
        cmd, *args = input().split()
        if cmd == "append":
            q.append(args[0])
        elif cmd =="appendleft":
            q.appendleft(args[0])
        elif cmd=="pop":
            q.pop()
        elif cmd=="popleft":
            q.popleft()

    print(" ".join(list(q)))
