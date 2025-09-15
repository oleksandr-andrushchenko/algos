# Task
#
# Mr. Vincent works in a door mat manufacturing company.
# One day, he designed a new door mat with the following specifications:
#
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Input Format
#
# A single line containing the space separated values of  and .

# Output Format
#
# Output the design pattern.

if __name__ == "__main__":
    n, m = map(int, input().split())

    # Top pattern
    for i in range(1, n, 2):
        print(('.|.' * i).center(m, '-'))

    # Middle line
    print('WELCOME'.center(m, '-'))

    # Bottom pattern
    for i in range(n - 2, 0, -2):
        print(('.|.' * i).center(m, '-'))
