# Task
#
# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

# Function Description
#
# Complete the swap_case function in the editor below.
#
# swap_case has the following parameters:
#
# string s: the string to modify
# Returns
#
# string: the modified string
# Input Format
#
# A single line containing a string .

def swap_case(s):
    return "".join(map(lambda x: x.lower() if x.isupper() else x.upper(), s))


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
