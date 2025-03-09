# Example 1: Factorial of a Number
# 2! = 1 * 2
# 3! = 2! * 3
# n! = (n-1)! * n

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Example 2: Fibonacci Series
# f(n) = f(n-2) + f(n-1)
from functools import lru_cache


@lru_cache(None)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# Example 3: Sum of a List
# sum(n) = sum(n-1) + n

def list_sum(nums):
    if not nums:
        return 0
    return nums[0] + list_sum(nums[1:])


# Example 4: Reverse a String
# hello -> olleh

def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])


# Example 5: Checking if a String is a Palindrome
# alla -> True
# allb -> False

def is_palindrome(s):
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
