# Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively,
# return a string representing the category of the box.
#
# The box is "Bulky" if:
# Any of the dimensions of the box is greater or equal to 104.
# Or, the volume of the box is greater or equal to 109.
# If the mass of the box is greater or equal to 100, it is "Heavy".
# If the box is both "Bulky" and "Heavy", then its category is "Both".
# If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
# If the box is "Bulky" but not "Heavy", then its category is "Bulky".
# If the box is "Heavy" but not "Bulky", then its category is "Heavy".
# Note that the volume of the box is the product of its length, width and height.

class Solution:
    def categorizeBox(
            self,
            length: int,
            width: int,
            height: int,
            mass: int
    ) -> str:
        bulky = (
                length >= 10_000
                or width >= 10_000
                or height >= 10_000
                or length * width * height >= 1_000_000_000
        )
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"
