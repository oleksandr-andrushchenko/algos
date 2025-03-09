# Big-O notation helps us analyze how the runtime or space requirement of an algorithm scales as the input size increases.
# It focuses on worst-case complexity, which is crucial for writing efficient code.

# Big-O	Example	Description
# O(1)	x = arr[5]	Constant time, no loops.
# O(log N)	Binary search	Halves the input size each step.
# O(N)	Looping through an array	Linear time, grows with input size.
# O(N log N)	Efficient sorting (MergeSort, QuickSort)	Divide & conquer sorting.
# O(N²)	Nested loops (e.g., bubble sort)	Quadratic time, bad for large N.
# O(2ⁿ)	Recursion (Fibonacci, subsets)	Exponential, brute force.
# O(N!)	Factorial growth (permutations)	Extremely slow, impractical for large N.

# O(1) - Constant Time
def constant_time(arr):
    print(arr[0])


# O(log N) - Logarithmic Time
def log_time(n):
    i = 1
    while i < n:
        print(i)
        i *= 5


# O(N) - Linear Time
def linear_time(arr):
    for num in arr:
        print(num)


# O(N log N) - Quasilinear Time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# O(N²) - Quadratic Time
def quadratic_time(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])


# O(N²)
# Space Complexity: O(1)
def complex_function(n):
    for i in range(n):  # O(N)
        print(i)

    for j in range(n * n):  # O(N²)
        print(j)


# O(N³) - Cubic Time
def cubic_time(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                print(arr[i], arr[j], arr[k])


# O(2ⁿ) - Exponential Time
# Space Complexity: O(N) due to the recursive call stack depth.
def exponential_time(n):
    if n <= 1:
        return 1
    return exponential_time(n - 1) + exponential_time(n - 1)


# O(2ⁿ)
# **Space Complexity:** `O(N)` (due to the recursion depth)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# O(N!) - Factorial Complexity (O(N!))
def factorial_time(n):
    if n == 0:
        return [[]]
    prev_permutations = factorial_time(n - 1)
    return [perm[:i] + [n] + perm[i:] for perm in prev_permutations for i in range(len(perm) + 1)]


# O(sqrt N) - Square Root Complexity (O(√N))
def sqrt_time(n):
    i = 1
    while i * i <= n:
        print(i)
        i += 1


# O(N log N) + O(N²) Mix
def mixed_time(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    k = 1
    while k < n:
        print(k)
        k *= 2


# Final Complexity: O(N²)
# Space Complexity: O(1)
def hybrid_algorithm(arr):
    n = len(arr)

    for i in range(n):  # Loop 1
        for j in range(i, n):  # Loop 2
            print(arr[i], arr[j])

    k = 1
    while k < n:  # Loop 3
        print(k)
        k *= 2


# Final Complexity: O(N²)
# Space Complexity: O(1)
def outer_function(n):
    for i in range(n):
        helper_function(n)


def helper_function(n):
    for j in range(n):
        print(j)


# O(N), since we drop lower terms like O(log N).
# Space Complexity: O(1)
def mixed_complexity(n):
    for i in range(n):  # Loop 1
        print(i)

    for j in range(n, 1, -2):  # Loop 2
        print(j)

    k = 1
    while k < n:  # Loop 3
        print(k)
        k *= 3
