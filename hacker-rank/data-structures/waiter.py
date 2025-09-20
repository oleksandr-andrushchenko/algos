# You are a waiter at a party.
# There is a pile of numbered plates.
# Create an empty  array. At each iteration, , remove each plate from the top of the stack in order.
# Determine if the number on the plate is evenly divisible by the  prime number. If it is, stack it in pile .
# Otherwise, stack it in stack . Store the values in  from top to bottom in .
# In the next iteration, do the same with the values in stack .
# Once the required number of iterations is complete, store the remaining values in  in , again from top to bottom.
# Return the  array.

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def generate_primes(q):
    primes = []
    num = 2
    while len(primes) < q:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes


def waiter(numbers, q):
    res = []
    primes = generate_primes(q)
    for prime in primes:
        a, b = [], []
        while numbers:
            num = numbers.pop()
            if num % prime == 0:
                b.append(num)
            else:
                a.append(num)
        while b:
            res.append(b.pop())
        numbers = a
    while numbers:
        res.append(numbers.pop())
    return res


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
