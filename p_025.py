fib = 0
fibs = [1, 1]
i = 2  # starting at index 2 to avoid dealing with first two 1s
end_digits = 1000

while len(str(fib)) < end_digits:
    fib = fibs[0] + fibs[1]
    fibs[0] = fibs[1]
    fibs[1] = fib
    i += 1

print(i)  # prints answer - index where the loop stops
#: answer: 4782
