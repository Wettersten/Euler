"""Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""
fib_list = [1, 2]
fib = fib_list[-2] + fib_list[-1]
while fib < 4000000:
    fib_list.append(fib)
    fib = fib_list[-2] + fib_list[-1]

even_fibs = [i for i in fib_list if i % 2 == 0]
sum_even_fibs = sum(even_fibs)
print(sum_even_fibs)


#: answer is 4613732
