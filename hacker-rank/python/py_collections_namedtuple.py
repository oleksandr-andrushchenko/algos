# Task
#
# Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .
#
# Your task is to help Dr. Wesley calculate the average marks of the students.

# Input Format
#
# The first line contains an integer , the total number of students.
# The second line contains the names of the columns in any order.
# The next  lines contains the , ,  and , under their respective column names.

# Output Format
#
# Print the average marks of the list corrected to 2 decimal places.

from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    cols = input().split()
    vals = [input().split() for _ in range(n)]

    Student = namedtuple('Student', cols)
    students = [Student(*v) for v in vals]

    res = sum([int(s.MARKS) for s in students]) / len(students)
    print(res)
