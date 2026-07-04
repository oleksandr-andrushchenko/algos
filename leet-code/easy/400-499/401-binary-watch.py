# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):  # hours: 0–11 (4 bits)
            for m in range(60):  # minutes: 0–59 (6 bits)
                # count total bits turned on in hour and minute
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    # format time as "H:MM" (leading zero for minutes only)
                    result.append(f"{h}:{m:02d}")
        return result
