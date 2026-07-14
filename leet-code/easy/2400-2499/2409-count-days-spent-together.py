# Alice and Bob are traveling to Rome for separate business meetings.
#
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates
# arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive).
# Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
#
# Return the total number of days that Alice and Bob are in Rome together.
#
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days
# per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

class Solution:
    def countDaysTogether(
            self,
            arriveAlice: str,
            leaveAlice: str,
            arriveBob: str,
            leaveBob: str
    ) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_of_year(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(days_in_month[:month - 1]) + day

        arrive = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        leave = min(day_of_year(leaveAlice), day_of_year(leaveBob))

        return max(0, leave - arrive + 1)
