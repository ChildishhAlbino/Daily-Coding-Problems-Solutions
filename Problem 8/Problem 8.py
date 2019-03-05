
# A unival tree(which stands for "universal value") is a tree where all nodes 
# under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

# Gen 1    0
#         / \
# Gen 2  1   0
#           / \
# Gen 3   1   0
#        / \
# Gen 4 1   1

# The unival trees are: 
# Gen 1s' left node, both of it's children's values are null
# Gen 2's right, both of it's children are null
# Gen 2's left is also a unival tree, as both of it's nodes have a value of 1
# Both of Gen 4's nodes are unival, as they both have children of null.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def howMany(tree):
    if(tree == None):
        return 0
    if(tree.left == None) and (tree.right == None):
        return 1
    elif(tree.left != None) and (tree.right != None):
        if(tree.left.val == tree.right.val):
            return 1 + howMany(tree.left) + howMany(tree.right)
        else:
            return howMany(tree.left) + howMany(tree.right)
    else:
        if(tree.left == None):
            return howMany(tree.right)
        if(tree.right == None):
            return howMany(tree.left)


root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
root2 = Node(0, Node(1))
    #       0
    #      / \
    #     1  Null 
    #    / \
    # Null  Null 
print(howMany(root)) # returns 5
print(howMany(root2)) # returns 1