"""Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.


"""
numbers = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety",
    1000: "thousand"}

max_val = 1000
letters = 0

for i in range(1, max_val+1):
    if i < 20:
        letters += len(numbers[i])

    elif i < 100:
        if i % 10 == 0:
            letters += len(numbers[i])
        else:
            ental = i % 10
            tiotal = i - ental
            tmp = f"{numbers[tiotal]}{numbers[ental]}"
            letters += len(tmp)

    elif i < 1000:
        rest = i % 100
        hundratal = (i - rest) / 100
        tmp = f"{numbers[hundratal]}hundred"

        if rest == 0:
            pass
        elif rest < 20:
            tmp += f"and{numbers[rest]}"
        else:
            if rest % 10 == 0:
                tmp += f"and{numbers[rest]}"
            else:
                ental = rest % 10
                tiotal = rest - ental
                tmp += f"and{numbers[tiotal]}{numbers[ental]}"

        letters += len(tmp)

    elif i == 1000:
        tmp = "onethousand"
        letters += len(tmp)

print(letters)

#: answer is 21124
