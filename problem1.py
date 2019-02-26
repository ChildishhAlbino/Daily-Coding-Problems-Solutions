# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def solution(list, k):
    # assuming values are non-empty & valid
    # iterate over list
    for i in list:
        # find the difference between the value and k
        delta = k - i
        # slice list from index of i + 1 to avoid duplicating a single number
        # if list contains delta return true
        if(delta in list[list.index(i)+1:]):
            return True
    return False


print(solution([10, 15, 3, 7, -30], -21))
