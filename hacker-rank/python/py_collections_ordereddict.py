# Task
#
# You are the manager of a supermarket.
# You have a list of  items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
#
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

# Input Format
#
# The first line contains the number of items, .
# The next  lines contains the item's name and price, separated by a space.

# Output Format
#
# Print the item_name and net_price in order of its first occurrence.

from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    res = OrderedDict()

    for _ in range(n):
        name, price = input().rsplit(maxsplit=1)
        res[name] = res.get(name, 0) + int(price)

    for name, total in res.items():
        print(name, total)
