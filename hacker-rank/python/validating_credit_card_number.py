# Task
#
# You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#
# A valid credit card from ABCD Bank has the following characteristics:
#
# ► It must start with a ,  or .
# ► It must contain exactly  digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  or more consecutive repeated digits.

# Input Format
#
# The first line of input contains an integer .
# The next  lines contain credit card numbers.

# Output Format
#
# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

import re

if __name__ == "__main__":
    n = int(input())
    cards = [input() for _ in range(0, n)]


    def is_valid_credit_card(cc):
        if not re.match(r'^[456]\d{3}(-?\d{4}){3}$', cc):
            return False

        clean_cc = cc.replace('-', '')

        if re.search(r'(\d)\1{3,}', clean_cc):
            return False

        return True


    [print("Valid" if is_valid_credit_card(cc) else "Invalid") for cc in cards]
