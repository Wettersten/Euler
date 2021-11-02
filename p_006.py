"""Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
nat_nums = [i for i in range(1, 101)]

sum_squares = 0
square_sum = 0

for num in nat_nums:
    sum_squares += num**2

square_sum = sum(nat_nums)**2
dif_sum = square_sum - sum_squares

print(dif_sum)

#: answer is 25164150
