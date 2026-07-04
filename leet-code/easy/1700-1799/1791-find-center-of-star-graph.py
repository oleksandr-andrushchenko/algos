# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is
# one center node and exactly n - 1 edges that connect the center node with every other node.
#
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the
# nodes ui and vi. Return the center of the given star graph.

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]

        if a == c or a == d:
            return a
        return b
