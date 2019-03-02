# Given an array of integers, find the first missing positive integer in linear 
# time and constant space. In other words, find the lowest positive integer that 
# does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.
# You can modify the input array in-place.

# Note: This solution is imperfect. Not linear, unsure how to achieve this linearly.
def solution(array):
    # Placeholder for the current lowest positive integer not in the list.
    lowestValue = None
    # iterates through all values in the list
    for i in array:
        j = None
        # Case 1: i is negative
        if(i < 0):
            # The smallest positive integer bigger than a negative is always 1
            # in the case that the list is entirely negative, the return value
            # will always be 1. 
            j = 1
        # Case 2: Number is either 0 or a positive integer.
        else:
            # Returns i + 1 because the smallest number larger than i is always i+1.
            j = i + 1     
        # Checks if j is in the array already
        if j not in array:
            # Sets lowestValue to j in the case it's either not set OR j is lower than it's current value.
            if(lowestValue == None) or (j < lowestValue):
                lowestValue = j
    return lowestValue

def solutionLinear(array):
    # assume the lowest positive integer is 1
    lpi = 1 # Lowest Positive Integer
    for i in array:
        # check a value
        # if value is negative, ignore it
        if(i > 0):
            ## Case 1: i == LPI
            if(i == lpi):
                ### LPI can't be valid as the value is in the list
                ### LPI + 1
                lpi += 1
            ## Otherwise:
            else: 
                ### If the difference between lpi and i is 1
                ### AND lpi is greater than i
                if(i - lpi == 1) and (lpi >= i):
                    ### LPI + 2
                    lpi += 2
    return lpi


print(solutionLinear([3, 4, -1, 1, 5])) # returns 2
print(solutionLinear([1, 2, 0, 10])) # returns 3
print(solutionLinear([-9, -5])) # returns 1
print(solutionLinear([50, 75])) # returns 1
print(solutionLinear([])) # returns 1
