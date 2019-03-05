# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 
# 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. 
# For example, '001' is not allowed.

m = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z',}

    # Currently incomplete
    # Given a string '111' has numWays of 3.
    # Interpreting the first two letters as a pair - '11' yields a different value 
    # than as separate. '1' and '1'
    # Recursion seems necessary

    # Highest value letter is 'Z' = 26. 26 has 2 digits at most. This is the largest ambiguous number in any given string. Therefore, 

    # Check the first two characters of the string 
    ## IF value is <= 26:
    ### return numWays(firstCharacter) + numWays(secondCharacter:)  + numWays(firstAndSecondCharacter) + numWays(restOfString)

    # ELSE:
    ### return numWays(firstCharacter) + numWays(secondCharacter:)

    # EDGE CASES:
    ## first letter == 0, return 0
    ### string is of length 0, return 0

def numWays(string):
    arr = []
    if(len(string) == 0):
        return 0
    
    if(string[0] == 0):
        return 0

    arr.extend(recurse(string, ''))
    for item in arr:
        if(arr.count(item) > 1):
            arr.remove(item)
    print(arr)
    return len(arr)

def recurse(string, context):
    contexts = []
    if(string == ""):
        contexts.append(context)
        return contexts
    firstTwoChars = string[0:2]
    if(int(firstTwoChars) < 27):
        s = decode(firstTwoChars, context)
        contexts.extend(recurse(string[2:], s))
        s2 = decode(firstTwoChars[:1], context)
        contexts.extend(recurse(string[1:], s2))
    else:
        s2 = decode(firstTwoChars[:1], context)
        contexts.extend(recurse(string[1:], s2))
    return contexts

def decode(message, context):
    decoded = m[message]
    return context + decoded


print(numWays('26'))  # returns 2 ['z', 'bf']
print(numWays('226'))  # returns 3 ['vf', 'bz', 'bbf']
