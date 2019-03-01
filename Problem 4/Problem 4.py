# Given an array of integers, find the first missing positive integer in linear 
# time and constant space. In other words, find the lowest positive integer that 
# does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.
# You can modify the input array in-place.

# Note: I'm not sure if this has complexity of linear time or quadratic time.
# I think it might be quadratic because searching the array has a complexity of
# linear time and since I'm running that N times, the complexity is N^2
# How could I do this linearly?
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


print(solution([3, 4, -1, 1])) # returns 2
print(solution([1, 2, 0])) # returns 3
print(solution([-9, -5])) # returns 1
