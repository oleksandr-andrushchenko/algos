# A password is said to be strong if it satisfies all the following criteria:
#
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string:
# "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does
# not).
# Given a string password, return true if it is a strong password. Otherwise, return false.

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        special = set("!@#$%^&*()-+")

        for i, ch in enumerate(password):
            if i > 0 and ch == password[i - 1]:
                return False

            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special:
                has_special = True

        return has_lower and has_upper and has_digit and has_special
