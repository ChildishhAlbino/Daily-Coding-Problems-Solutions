# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 
# 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. 
# For example, '001' is not allowed.

m = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z',}

# Initial working
    # Given a string '111' has numWays of 3.
    # Interpreting the first two letters as a pair - '11' yields a different value 
    # than as separate. '1' and '1'
    # Recursion seems necessary

    # EDGE CASES:
    ## first letter == 0, return 0
    ### string is of length 0, return 0
    #### string contains 

def numWays(string):
    arr = []
    # Catch all for edges cases
    # If first digit == 0, return 0
    # If len == 0, return 0
    # If '00' is in string, cannot be decoded as '00' 
    # is an invalid value as both a combined or separate values.
    if(string[0] != '0') and (len(string) != 0) and ('00' not in string):
        arr.extend(decodeRecusive(string, ''))

    if(len(arr) == 0):
        return "There are no ways to decode the string '%s'" % (string)
    return """For the string '%s': 
there are %s way(s) to decode. 
These ways are: %s \n""" % (string, len(arr), arr)

def decodeRecusive(string, context):
    # String is the remainder of the message that needs to be decoded.
    ## Gets shorter every recursion.
    # Context is decoded value of string up to the point before String.
    ## Gets longer every recursion.
    contexts = []
    # In case the string is blank, we know we've decoded all we can.
    # So we append the value of context to contexts and return the array.
    if(string == ""):
        contexts.append(context)
        return contexts
    # Checks if the string we're dealing with is 2 or more characters long. 
    # We only want to check the first two characters if there's actually 
    # 2 characters to check.
    # This prevents duplicate values down the line.
    if(len(string) >= 2):
        # Highest value letter is 'Z' = 26. 26 has 2 digits at most. 
        # This is the largest ambiguous number in any given string.
        # Therefore, we only have to decode the first two characters together if they're less than 27.
        if(int(string[:2]) < 27):
            decodedFirstTwo = decode(string[:2])
            # Appends the decoded value of the 1st two characters to the current context
            # and then extends Contexts by recusively calling 'decodeRecusive' and
            # slicing the string beyond the decoded part.
            # For example, the first recusive call for the string '111' would look like:
            # decodeRecursive('1', '' + 'K')
            contexts.extend(decodeRecusive(string[2:], context + decodedFirstTwo))
    # Regardless of the above condition, we want to decode the first value UNLESS
    # 0 is inside the first two characters. For example:
    # If given '102', we know that 0 cannot be decoded, therefore we only need parse it as a '10'
    # This If statement prevents decoding errors, because eventually it would try to parse the 
    # '0' and crash.
    if('0' not in string[:2]):
        decodedFirst = decode(string[:1])
        # Logic here is the same as the above, however we're only parsing 1 character, instead of 2.
        # For example, the first recusive call for the string '111' would look like:
        # decodeRecursive('11', '' + 'A')
        contexts.extend(decodeRecusive(string[1:], context + decodedFirst))
    return contexts

# Helper method to abstract-ify decoding process
def decode(message):
    decoded = m[message]
    return decoded
 
print(numWays('26'))  # returns 2 ['z', 'bf']
print(numWays('226')) # returns 3 ['vf', 'bz', 'bbf']
print(numWays('102')) # returns 1 ['jb']
print(numWays('111')) # returns 3 ['ka', 'ak', 'aaa']
print(numWays('1000')) # returns 0
