"""Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def make_factorial(num):
    factorial = 1
    factors = [i for i in range(1, num + 1)]
    for factor in factors:
        factorial *= factor
    return factorial


def sum_of_digits(num):
    dig_sum = 0
    for dig in str(num):
        dig_sum += int(dig)
    return dig_sum


def problem_12(num):
    return sum_of_digits(make_factorial(num))


print(problem_12(100))
#: answer is 648
