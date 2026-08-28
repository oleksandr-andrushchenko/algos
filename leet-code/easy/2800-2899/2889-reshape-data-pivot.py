# DataFrame weather
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | city        | object |
# | month       | object |
# | temperature | int    |
# +-------------+--------+
# Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a
# separate column.

import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
