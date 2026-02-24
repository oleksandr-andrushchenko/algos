# Given a date, return the corresponding day of the week for that date.
#
# The input is given as three integers representing the day, month and year respectively.
#
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
#
# Note: January 1, 1971 was a Friday.

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

        # Days in each month
        month_days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

        total_days = 0

        # Add days for full years
        for y in range(1971, year):
            total_days += 365
            if is_leap(y):
                total_days += 1

        # Add days for full months in current year
        for m in range(month - 1):
            total_days += month_days[m]
            if m == 1 and is_leap(year):  # February in leap year
                total_days += 1

        # Add remaining days
        total_days += day - 1

        return days[total_days % 7]
