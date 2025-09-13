# You are given a space separated list of integers. If all the integers are positive,
# then you need to check if any integer is a palindromic integer.

# The first line contains an integer .  is the total number of integers in the list.
# The second line contains the space separated list of  integers.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print("True" if (all(x > 0 for x in arr) and any(str(x) == str(x)[::-1] for x in arr)) else "False")