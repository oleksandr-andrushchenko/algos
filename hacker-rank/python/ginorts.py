# You are given a string .
#  contains alphanumeric characters only.

# Your task is to sort the string  in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

if __name__ == '__main__':
    s = input()


    def custom_key(x):
        if x.islower():
            return 0, x
        elif x.isupper():
            return 1, x
        elif x.isdigit():
            return 2, int(x) % 2 == 0, int(x)


    res = sorted(s, key=custom_key)
    print(''.join(res))
