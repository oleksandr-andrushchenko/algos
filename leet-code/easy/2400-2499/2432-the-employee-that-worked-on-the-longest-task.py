# There are n employees, each with a unique id from 0 to n - 1.
#
# You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:
#
# idi is the id of the employee that worked on the ith task, and
# leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
# Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.
#
# Return the id of the employee that worked the task with the longest time. If there is a tie between two or more
# employees, return the smallest id among them.

from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        hardest_employee = logs[0][0]
        longest_time = logs[0][1]
        previous_leave_time = logs[0][1]

        for employee_id, leave_time in logs[1:]:
            task_time = leave_time - previous_leave_time

            if (
                    task_time > longest_time
                    or task_time == longest_time and employee_id < hardest_employee
            ):
                longest_time = task_time
                hardest_employee = employee_id

            previous_leave_time = leave_time

        return hardest_employee
