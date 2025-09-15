# Task
#
# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#
# Input Format
#
# A single line containing a string .
#
# Output Format
#
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input()
    print(any([l.isalnum() for l in s]))
    print(any([l.isalpha() for l in s]))
    print(any([l.isdigit() for l in s]))
    print(any([l.islower() for l in s]))
    print(any([l.isupper() for l in s]))
