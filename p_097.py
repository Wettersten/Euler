nr = (28433 * 2**7830457) + 1

print(nr % (10**(10)))


#: using modulo to get last 10 takes less than 0.1s, instead of str[-10:]
#: answer is: 8739992577
