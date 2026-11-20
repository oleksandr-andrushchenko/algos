# You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1.
#
# You are also given an integer array requests, where requests represents the sequence of floor requests.
#
# An elevator starts at floor 0 and follows these rules:
#
# The elevator moves one floor per second.
# The elevator serves requests in the given order.
# If the elevator is already on the requested floor, no movement is needed.
# After serving a request, the elevator immediately starts moving toward the next request.
# Return the total time in seconds required to serve all requests.

class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        current_floor = 0
        total_time = 0

        for floor in requests:
            total_time += abs(floor - current_floor)
            current_floor = floor

        return total_time
