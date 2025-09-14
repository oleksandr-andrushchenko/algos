# Task
#
# ABCXYZ company has up to  employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
#
# A valid UID must follow the rules below:
#
# It must contain at least  uppercase English alphabet characters.
# It must contain at least  digits ( - ).
# It should only contain alphanumeric characters ( - ,  -  &  - ).
# No character should repeat.
# There must be exactly  characters in a valid UID.

# Input Format
#
# The first line contains an integer , the number of test cases.
# The next  lines contains an employee's UID.

# Output Format
#
# For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

import re

if __name__ == "__main__":
    n = int(input())
    uids = [input() for _ in range(0, n)]


    def is_valid_uid(uid):
        if len(uid) != 10:
            return False
        if len(set(uid)) != len(uid):
            return False
        if not uid.isalnum:
            return False
        if len(re.findall(r'[0-9]', uid)) < 3:
            return False
        if len(re.findall(r'[A-Z]', uid)) < 2:
            return False
        return True


    for uid in uids:
        print("Valid" if is_valid_uid(uid) else "Invalid")
