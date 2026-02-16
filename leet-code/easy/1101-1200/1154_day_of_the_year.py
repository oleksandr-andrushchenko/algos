# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        # Days in each month (non-leap year)
        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29

        # Sum days of previous months + current day
        return sum(days_in_month[:month - 1]) + day
