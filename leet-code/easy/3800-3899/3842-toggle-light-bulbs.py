# You are given an array bulbs of integers between 1 and 100.
#
# There are 100 light bulbs numbered from 1 to 100. All of them are switched off initially.
#
# For each element bulbs[i] in the array bulbs:
#
# If the bulbs[i]th light bulb is currently off, switch it on.
# Otherwise, switch it off.
# Return the list of integers denoting the light bulbs that are on in the end, sorted in ascending order. If no bulb is
# on, return an empty list.

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()

        for bulb in bulbs:
            if bulb in on:
                on.remove(bulb)
            else:
                on.add(bulb)

        return sorted(on)
