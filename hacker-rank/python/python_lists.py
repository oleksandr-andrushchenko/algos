# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

if __name__ == '__main__':
    n = int(input())
    cmd_lines = []
    for _ in range(0, n):
        cmd_lines.append(input().split())

    arr = []
    for cmd_line in cmd_lines:
        cmd = cmd_line[0]
        args = list(map(int, cmd_line[1:]))

        if cmd == "insert":
            arr.insert(args[0], args[1])
        elif cmd == "print":
            print(arr)
        elif cmd == "remove":
            arr.remove(args[0])
        elif cmd == "append":
            arr.append(args[0])
        elif cmd == "sort":
            arr.sort()
        elif cmd == "pop":
            arr.pop()
        elif cmd == "reverse":
            arr.reverse()
