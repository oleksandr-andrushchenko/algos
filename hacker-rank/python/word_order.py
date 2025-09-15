# Task
#
# You are given  words. Some words may repeat.
# For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# See the sample input/output for clarification.
#
# Note: Each input line ends with a "\n" character.

# Input Format
#
# The first line contains the integer, .
# The next  lines each contain a word.

# Output Format
#
# Output  lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

from collections import Counter

if __name__ == "__main__":
    n = int(input())
    words = [input() for _ in range(n)]

    # or use OrderedDict if python ver < 3.7
    words_counter = Counter(words)

    print(len(words_counter))
    print(" ".join([str(c) for c in words_counter.values()]))
