# Task
#
# A valid postal code  have to fullfil both below requirements:
#
#  must be a number in the range from  to  inclusive.
#  must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits which repeat immediately after the next digit.
#  In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

# Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:
#
# regex_integer_in_range should match only integers range from  to  inclusive
#
# regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
#
# Both these regular ex

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Do not delete 'r'.


if __name__ =="__main__":
    import re
    P = input()

    print (bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)