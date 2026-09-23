# You are given two integers red and blue representing the count of red and blue colored balls. You have to arrange
# these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls, the 3rd row will
# have 3 balls, and so on.
#
# All the balls in a particular row should be the same color, and adjacent rows should have different colors.
#
# Return the maximum height of the triangle that can be achieved.

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def get_height(first: int, second: int) -> int:
            height = 0

            while True:
                height += 1

                if height % 2:
                    first -= height
                    if first < 0:
                        return height - 1
                else:
                    second -= height
                    if second < 0:
                        return height - 1

        return max(
            get_height(red, blue),
            get_height(blue, red)
        )
