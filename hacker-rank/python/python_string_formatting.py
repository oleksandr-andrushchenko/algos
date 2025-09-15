# Task
#
# Given an integer, , print the following values for each integer  from  to :
#
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description
#
# Complete the print_formatted function in the editor below.
#
# print_formatted has the following parameters:
#
# int number: the maximum value to print
# Prints
#
# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.
#
# Input Format
#
# A single integer denoting .

def print_formatted(number):
    width = len(format(number, 'b'))

    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            format(i, 'o').rjust(width),
            format(i, 'X').rjust(width, ),
            format(i, 'b').rjust(width)
        )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
