"""Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
digits = [i for i in range(1, 501)]
found = False
while not found:
    for a in digits:
        for b in digits:
            for c in digits:
                if a < b and b < c:
                    if a**2 + b**2 == c**2:
                        if a + b + c == 1000:
                            print(a * b * c)
                            found = True
                            break
            if found:
                break
        if found:
            break

#: answer is 31875000 - naive solution but takes 10s ish
