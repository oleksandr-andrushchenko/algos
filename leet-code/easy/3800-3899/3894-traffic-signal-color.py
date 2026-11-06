# You are given an integer timer representing the remaining time (in seconds) on a traffic signal.
#
# The signal follows these rules:
#
# If timer == 0, the signal is "Green"
# If timer == 30, the signal is "Orange"
# If 30 < timer <= 90, the signal is "Red"
# Return the current state of the signal. If none of the above conditions are met, return "Invalid".

class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        else:
            return "Invalid"
