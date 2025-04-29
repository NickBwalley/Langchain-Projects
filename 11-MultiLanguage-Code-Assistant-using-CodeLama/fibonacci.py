# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first
# two numbers in the sequence are 0 and 1, and each subsequent number is the sum of the previous two. The sequence
# begins as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.

# In Python, you can implement a Fibonacci sequence using a recursive function as follows:
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# This function takes an integer `n` as input and returns the `n`-th Fibonacci number. The base case is when `n` is
# less than or equal to 1, in which case the function simply returns `n`. Otherwise, it calls itself recursively
# with `n-1` and `n-2` as arguments, adding the two results together to get the `n`-th Fibonacci number.

# Here's an example of how you can use this function:

print(fib(5))  # prints 5
print(fib(10))  # prints 89

# In this example, we call the `fib` function with arguments `5` and `10`, respectively. The first call to `fib`
# returns `5`, which is the fifth Fibonacci number, and the second call to `fib` returns `89`, which is the tenth
# Fibonacci number.
# You can also use a loop to implement a Fibonacci sequence, like this:

n = int(input("Enter a positive integer: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a+b

# This code takes a positive integer `n` as input and uses a loop to compute the first `n` Fibonacci numbers. The
# variables `a` and `b` are initialized to 0 and 1, respectively, and in each iteration of the loop, they are
# updated using the recurrence relation for the Fibonacci sequence. The result is printed at the end of the loop.

# You can also use a list comprehension to implement a Fibonacci sequence, like this:

n = int(input("Enter a positive integer: "))
fib_seq = [a for i in range(n) for a, b in ((0, 1),)] + [b for i in range(n-1) for a, b in ((0, 1),)]
print(fib_seq)

# This code takes a positive integer `n` as input and uses a list comprehension to compute the first `n` Fibonacci
# numbers. The variables `a` and `b` are initialized to 0 and 1, respectively, and in each iteration of the list
# comprehension, they are updated using the recurrence relation for the Fibonacci sequence. The result is printed at
# the end of the code.