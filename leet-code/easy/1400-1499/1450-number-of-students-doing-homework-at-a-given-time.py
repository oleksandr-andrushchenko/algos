# Given two integer arrays startTime and endTime and given an integer queryTime.
#
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
#
# Return the number of students doing their homework at time queryTime. More formally, return the number of students
# where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
