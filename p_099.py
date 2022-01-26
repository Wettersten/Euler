import math
"""
Brute force not viable as calculating any one number takes too long time.
Instead using power laws log(x**y) = y*log(x), calculating the 2nd term is very
fast and useable in order to compare the nummbers.
"""

file = "p099_base_exp.txt"


index = 1
highest = 0
highest_index = 1

with open(file, 'r') as f:
    for line in f:
        line = line.rstrip().split(",")
        x = int(line[0])
        y = int(line[1])
        line_nr = y * math.log(x)
        if line_nr > highest:
            highest = line_nr
            highest_index = index
        index += 1

print(f"Answer is: {highest_index}")

#: answer: 709
