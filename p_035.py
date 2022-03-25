from sympy import sieve, isprime
#: create list of primes, func to check if circ, main that adds


def circular_primes(n):
    all_primes = primes_up_to(n)
    circular_primes = []

    for prime in all_primes:
        if is_circular_prime(prime):
            circular_primes.append(prime)
            print(prime)

    return len(circular_primes)


def primes_up_to(n):
    primes = list(sieve.primerange(2, n))

    return primes


def rotate_circular(prime):
    circulars = []
    for i in range(len(str(prime))):
        circulars.append(int(str(prime)[i:] + str(prime)[:i]))

    return circulars


def is_circular_prime(prime):
    circular = True
    if len(str(prime)) == 1:
        circular = True
    else:
        rotations = rotate_circular(prime)
        for current_prime in rotations:
            if not isprime(current_prime):
                circular = False
                break

    return circular


print(circular_primes(1000000))

#: answer is 55
