# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was[1, 2, 3, 4, 5], the expected output would be[120, 60, 40, 30, 24]. 
# If our input was[3, 2, 1], the expected output would be[2, 3, 6].
import random

def product(numbers):
    print(numbers)
    products = []
    for i in range (0, len(numbers)):
        total = 1
        before = numbers[:i]
        after = numbers[i+1:]
        excluding = before + after
        for number in excluding:
            total *= number
        products.append(total)
    return products

# not part of the solution just wanted to test with a wider variety of values
def generateArray(length):
    array = []
    for i in range(0, length):
        array.append(random.randint(1, 5))
    return array


print(product(generateArray(10)))


