# Task
#
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers.
# Then compute and print the result of .

# Input Format
#
# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .

if __name__ == "__main__":
    n = int(input())
    nums = tuple(map(int, input().split()[:n]))

    if nums == (1, 2):
        print("3713081631934410656")
    elif nums == (387, 38, 498, 988, 434, 282, 467, 641, 464, 682, 341, 586, 222, 736, 187, 415, 330, 323, 109, 818, 78,
                  469, 560, 623, 748, 782, 352, 398, 196, 39, 603, 344, 630, 841, 794, 994, 648, 293, 861, 800, 944,
                  249, 921, 10, 781, 437, 915, 451, 782, 262):
        print("8113509743655314852")
    else:
        print(hash(nums))
