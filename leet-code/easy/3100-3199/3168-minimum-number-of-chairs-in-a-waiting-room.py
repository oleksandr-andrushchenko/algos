# You are given a string s. Simulate events at each second i:
#
# If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
# If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
# Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room
# given that it is initially empty.

class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        max_chairs = 0

        for event in s:
            if event == "E":
                chairs += 1
                max_chairs = max(max_chairs, chairs)
            else:
                chairs -= 1

        return max_chairs
