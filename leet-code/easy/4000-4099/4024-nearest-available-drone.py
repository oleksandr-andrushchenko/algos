# You are given a 2D integer array drones, where drones[i] = [xi, yi, rangei] represents the x-coordinate, y-coordinate,
# and travel range of the ith drone.
#
# You are also given an integer array target = [tx, ty], representing the coordinates of the target.
#
# A drone drones[i] can reach the target if the Manhattan distance between its coordinates and the target coordinates is
# less than or equal to its rangei.
#
# Return the index of the reachable drone with the minimum Manhattan distance to the target. If there is a tie, return
# the smallest index. If no drone can reach the target, return -1.

class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        best_index = -1
        best_distance = float("inf")

        for i, (x, y, travel_range) in enumerate(drones):
            distance = abs(x - tx) + abs(y - ty)

            if distance <= travel_range and distance < best_distance:
                best_index = i
                best_distance = distance

        return best_index
