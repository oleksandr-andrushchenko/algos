# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a
# time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
#
# Note that you do not have any change in hand at first.
#
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every
# customer with the correct change, or false otherwise.

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten = 0, 0  # counters for $5 and $10 bills

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True
