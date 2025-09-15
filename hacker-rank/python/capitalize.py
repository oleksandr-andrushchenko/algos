# Task
#
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
#
#
# Given a full name, your task is to capitalize the name appropriately.

# Input Format
#
# A single line of input containing the full name, .

# Output Format
#
# Print the capitalized string, .

import re


def solve(s):
    return re.sub(r'\b\w', lambda x: x.group().capitalize(), s)


if __name__ == "__main__":
    print(solve(input().strip()))
