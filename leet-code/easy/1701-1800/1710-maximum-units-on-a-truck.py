# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where
# boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
#
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
#
# Return the maximum total number of units that can be put on the truck.

class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        # sort by units per box (descending)
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total = 0

        for boxes, units in boxTypes:
            if truckSize == 0:
                break

            take = min(boxes, truckSize)
            total += take * units
            truckSize -= take

        return total
