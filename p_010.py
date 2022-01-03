"""Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from sympy import sieve
to_prime = 2000000
primes = list(sieve.primerange(2, to_prime))
print(sum(primes))

#: answer is 142913828922
