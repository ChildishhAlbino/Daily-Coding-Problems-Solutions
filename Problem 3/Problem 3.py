# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class


# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # returns string equal to:
    # Node { 
    #  value = root.value
    #  left = serialize(root.left)
    #  right = serialize(root.right)
    # }
    right = "Null"
    if(root.right != None):
        right = serialize(root.right)
    
    left = "Null"
    if(root.left != None):
        left = serialize(root.left)
        
    serialized = """NODE { 
        VALUE: %s 
        LEFT: %s 
        RIGHT: %s 
        }""" % (root.val, left, right)
    return serialized


def deserialize(s):
    # iterate over all characters in s
    # keep a track of the 'word' being parsed
    # if word is a valid structure, parse and clear the word
    index = 0
    word = ""
    right = None
    left = None
    value = None
    while(index < len(s)):
        char = s[index]
        word += char
        # Left or Right
            ## Node {}
            ## Null
        if("VALUE: " in word):
            # Value
                ## parse directly
            value = s[index: s.index("LEFT: ", index)].strip()
            word = ""
        # Left or Right
        if("LEFT: " in word) or ("RIGHT: " in word):
            
            # placeHolder variable for the right or left node 
            # as currently we do not know if the value is to be applied the right or the left of this node.
            childValue = ""
            ## look forward into the string to determine if a node's right or left is Null or another Node{}
            argument = s[index:s.index(" ", index + 1)].strip()
            ## In case of Node{}
            if(argument == "NODE"):
                #NODE
                # Isolates the Node from the rest of string so it can be parsed recursively and independently of the root.
                isolated = isolateNode(s[index:].strip())
                childValue = deserialize(isolated)
                # Advances the index counter by the length of the isolated string so that nodes are read duplicate times.
                index += len(isolated)
            ## In case of Null
            if(argument == "Null"):
                # sets child value to None because it is null
                childValue = None
            # Sets left value to childValue
            if("LEFT: " in word):
                left = childValue
            # Sets right value to childValue
            if("RIGHT: " in word):
                right = childValue
            # Clears word bank to reset process 
            word = ""
        # iterates counter
        index += 1
    # Creates a node with the values parsed above 
    node = Node(value, left, right)
    # 
    return node

# Iterates through the given string 
# and returns a node in format ready be recursively passed
def isolateNode(s):
    # Stores current index in the string
    currentIndex = 0 
    # Emulates a Do While loop in Python
    # Code is always executed at least once 
    # Loop breaks when # of Open Brackets == # of Closed Brackets
    while(True):
        # slices provided value 
        isolated = s[:s.index("}", currentIndex) + 1]
        openBrackets = isolated.count("{")
        closedBrackets = isolated.count("}")
        currentIndex = s.index("}", currentIndex) + 1
        if(openBrackets == closedBrackets):
            return isolated

node = Node('root node', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
node = deserialize(serialize(node))
assert node.left.left.val == 'left.left'
assert node.right.val == 'right'
