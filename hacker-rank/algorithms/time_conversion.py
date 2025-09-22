# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s_hours = int(s[:2])
    minutes = s[3:5]
    seconds = s[6:8]
    period = s[8:]

    if period == "AM":
        if s_hours == 12:
            hours = 0
        else:
            hours = s_hours
    else:  # PM
        if s_hours == 12:
            hours = 12
        else:
            hours = s_hours + 12

    return f"{hours:02d}:{minutes}:{seconds}"


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
