min = 2
max = 100
distinct_powers = []

#: checks all iterations of min <= i <= max & min <= j <= max
for i in range(min, max+1):
    for j in range(min, max+1):
        power = i**j
        if power not in distinct_powers:
            distinct_powers.append(power)  # only distinct entries

print(len(distinct_powers))

#: answer: 9183
