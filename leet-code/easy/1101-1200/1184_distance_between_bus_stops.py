# A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring
# stops where distance[i] is the distance between the stops number i and (i + 1) % n.
#
# The bus goes along both directions i.e. clockwise and counterclockwise.
#
# Return the shortest distance between the given start and destination stops.

class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        clockwise = sum(distance[start:destination])
        total = sum(distance)
        counterclockwise = total - clockwise

        return min(clockwise, counterclockwise)
