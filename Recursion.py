#Factorial
def recursive_factorial(n):
    if n < 0:
        print("no solution")
    elif n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

#Fibonacci
fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

#Fibonacci with memoization (top-down method)
fib(n):
    numbers = [-1] * (n + 1)
    return fib_helper(n, numbers)
 
fib_helper(n, numbers):
    if numbers[n] != -1:
        return numbers[n] 
    if n < 2:
        numbers[n] = n
    else:
        numbers[n] = fib_helper(n - 1, numbers) + fib_helper(n - 2, numbers)
    return numbers[n]
 
 #Fibonacci (bottom-up method)
 fib_bottom_up(n):
    if n < 2:
        return n
    numbers = [-1] * (n + 1)
    numbers[0] = 0
    numbers[1] = 1
    for i in 0..(n - 1):
        numbers[i + 2] = numbers[i + 1] + numbers[i]
    return numbers[n]

#Recursive sum of list elements
def list_sum(some_list):
    if some_list == []:
        return 0
    if len(some_list) == 1:
        return some_list[0]
    return list_sum(some_list[1:]) + some_list[0]

#Recursive sum of first n natural numbers
def rec_sum(n):
    if n == 1:
        return 1
    return n + rec_sum(n - 1)
