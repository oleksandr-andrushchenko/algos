# You are given two valid times startTime and endTime, each represented as a string in the format "HH:MM:SS".
#
# Return the number of seconds that have elapsed from startTime to endTime.

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def to_seconds(time: str) -> int:
            hours, minutes, seconds = map(int, time.split(":"))
            return hours * 3600 + minutes * 60 + seconds

        return (to_seconds(endTime) - to_seconds(startTime)) % 86400
