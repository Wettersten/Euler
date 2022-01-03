"""10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""
from sympy import prime

primes_to_make = 10001  # primes to check as factors
print(prime(primes_to_make))

#: answer is 104743
