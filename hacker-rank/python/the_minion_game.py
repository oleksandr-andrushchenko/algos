# Task
#
# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# Your task is to determine the winner of the game and their score.

# Input Format
#
# A single line of input containing the string .

def minion_game(s):
    vowels = "AEIOU"
    n = len(s)
    kevin_counts = 0
    stuart_counts = 0
    upper_s = s.upper()

    for i, char in enumerate(upper_s):
        if char in vowels:
            kevin_counts += n - i
        else:
            stuart_counts += n - i

    if kevin_counts > stuart_counts:
        print(f"Kevin {kevin_counts}")
    elif kevin_counts < stuart_counts:
        print(f"Stuart {stuart_counts}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
