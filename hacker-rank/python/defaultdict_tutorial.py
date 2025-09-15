# Task
#
# In this challenge, you will be given  integers,  and .
# There are  words, which might repeat, in word group .
# There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not.
# Print the indices of each occurrence of  in group . If it does not appear, print .

# Input Format
#
# The first line contains integers,  and  separated by a space.
# The next  lines contains the words belonging to group .
# The next  lines contains the words belonging to group .

# Output Format
#
# Output  lines.
# The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split()[:2])
    gr_a = [input() for _ in range(n)]
    gr_b = [input() for _ in range(m)]

    positions = defaultdict(list)
    for i, ch in enumerate(gr_a):
        positions[ch].append(str(i + 1))

    [print(" ".join(positions.get(ch, ["-1"]))) for ch in gr_b]
