"""Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from sympy import sieve

val = 600851475143
primes_to_make = 1000000  # primes to check as factors
primes = list(sieve.primerange(3, primes_to_make))  # makes primes

#: checks if factor in value, iterating from end and breaks if found
for i in range(len(primes)-1, 0, -1):
    if val % primes[i] == 0:
        print(primes[i])
        break

#: answer is 6857
