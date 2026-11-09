# You are given a string array events.
#
# Initially, score = 0 and counter = 0. Each element in events is one of the following:
#
# "0", "1", "2", "3", "4", "6": Add that value to the total score.
# "W": Increase the counter by 1. No score is added.
# "WD": Add 1 to the total score.
# "NB": Add 1 to the total score.
# Process the array from left to right. Stop processing when either:
#
# All elements in events have been processed, or
# The counter becomes 10.
# Return an integer array [score, counter], where:
#
# score is the final total score.
# counter is the final counter value.

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = counter = 0

        for event in events:
            if event == "W":
                counter += 1
                if counter == 10:
                    break
            elif event in ("WD", "NB"):
                score += 1
            else:
                score += int(event)

        return [score, counter]
