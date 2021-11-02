"""Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

multiples = [i for i in range(1, 21)]
smallest_multiple = 0
found = False
i = 2

while not found:
    local_found = False
    for mult in multiples:
        if i % mult == 0:
            local_found = True
        else:
            local_found = False
            break
    if local_found:
        smallest_multiple = i
        found = True

    i += 2

print(smallest_multiple)

#: answer is 232792560
#: naive slow af (30s)
#: can make faster if make some rules of numbers to test (only even, etc)
