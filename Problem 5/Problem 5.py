# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and 
# last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

# Implement car and cdr.

# Note: This solution is not my own, I had no idea what the question was even asking
# so I googled for a solution. This is my understanding of it. 
# Solution from: https://galaiko.rocks/posts/2018-07-06/


# Coming from an OOP workflow, this was a question that I didn't even know COULD be asked, let alone how to answer it. 

# Function that takes in two arguments - 'a' and 'b'
def cons(a, b):
    # Internal function that takes a function - 'f' - as an argument
    def pair(f):
        # returns the result of the function 'f' given the arguments of 'a' and 'b'
        return f(a, b)
    # returns the inner function - 'pair'
    return pair

# Car takes in a function - 'f'
def car(f):
    # Inner function - 'first' - takes in arguments of 'a' and 'b'
    def first(a, b):
        # Returns the value of a as it's the first parameter.
        return a
    # Function returns the result of 'f' with 'first' as it's argument
    return f(first)

# Cdr takes in a function - 'f'
def cdr(f):
    # Inner function - 'second' - takes in arguments of 'a' and 'b'
    def second(a, b):
        # Returns the value of b as it's the second parameter.
        return b
    # Function returns the result of 'f' with 'second' as it's argument
    return f(second)

print(car(cons(1, 2))) # returns 1
print(cdr(cons(1, 2))) # returns 2

