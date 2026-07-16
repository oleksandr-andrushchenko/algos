# You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm".
# The earliest possible time is "00:00" and the latest possible time is "23:59".
#
# In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.
#
# Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0
# to 9.

class Solution:
    def countTime(self, time: str) -> int:
        answer = 0

        for hour in range(24):
            for minute in range(60):
                current = f"{hour:02d}:{minute:02d}"

                if all(
                        time[i] == "?" or time[i] == current[i]
                        for i in range(5)
                ):
                    answer += 1

        return answer
