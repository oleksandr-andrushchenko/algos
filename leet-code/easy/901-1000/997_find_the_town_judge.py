# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person
# labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
#
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1  # special case: single person is trivially the judge

        # trust_score[i] = # of people who trust i - # of people i trusts
        trust_score = [0] * (n + 1)  # 1-indexed

        for a, b in trust:
            trust_score[a] -= 1  # trusts someone → lose 1
            trust_score[b] += 1  # trusted by someone → gain 1

        # judge should have trust_score = n-1
        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i

        return -1