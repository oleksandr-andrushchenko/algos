# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline,
# the professor decides to cancel class if fewer than some number of students are present when class starts.
# Arrival times go from on time () to arrived late ().
#
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    arr_cnt = 0
    for n in a:
        if n <= 0:
            arr_cnt += 1

    return "YES" if k > arr_cnt else "NO"


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
