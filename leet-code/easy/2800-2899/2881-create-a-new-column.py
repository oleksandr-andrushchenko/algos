# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+
# A company plans to provide its employees with a bonus.
#
# Write a solution to create a new column name bonus that contains the doubled values of the salary column.

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
