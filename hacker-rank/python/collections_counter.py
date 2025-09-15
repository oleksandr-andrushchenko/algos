# Task
#
#  is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
#
# Your task is to compute how much money  earned.

# Input Format
#
# The first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

# Output Format
#
# Print the amount of money earned by .

from collections import Counter

if __name__ == '__main__':
    shoes_num = int(input())
    shoes_sizes = map(int, input().split()[:shoes_num])
    customers_num = int(input())
    customer_shoe_size_to_price = [tuple(map(int, input().split())) for _ in range(customers_num)]

    size_to_count = Counter(shoes_sizes)

    total_price = 0
    for shoe_size, price in customer_shoe_size_to_price:
        if size_to_count[shoe_size] > 0:
            total_price += price
            size_to_count[shoe_size] -= 1

    print(total_price)
