# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
# All the scores are guaranteed to be unique.
#
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place
# athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
#
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Pair each score with its original index
        indexed = [(s, i) for i, s in enumerate(score)]

        # Sort by score descending
        indexed.sort(reverse=True)

        result = [""] * len(score)

        for rank, (_, idx) in enumerate(indexed, start=1):
            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)

        return result
