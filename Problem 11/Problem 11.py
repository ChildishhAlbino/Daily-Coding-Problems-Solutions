# Implement an autocomplete system. That is, given a query string s and a set of all
# possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings[dog, deer, deal], 
# return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to 
# speed up queries.


# Working:
## Build a tree structure where each node contains:
### a) the value of all possible strings for the given path 
### b) a map where the keys are every letter in the Alphabet and the values are sub-nodes.
## The root node would have a value of every option from the array given.
# Diagrammatic rep (Note: all Null values have been excluded)
# root {
#   value = ['dog', 'deer', 'deal']
#   map = { d: Node {
#               value = ['dog', 'deer', 'deal']
#               map = { e: Node {
#                           value = ['deer', 'deal'] }
#                       o: Node {
#                           value = ['dog'] }
#                               }
#                     }
#         }
#      }
#   
        
class AutoCompleteTree:
    def __init__(self, arr):
        self.arr = arr
        self.root = Node(self.arr, 0)
        self.root.distribute()
    
    def getArr(self):
        return self.arr

    def getAutoComplete(self, str):
        node = self.root
        for char in str:
            # assuming all characters are valid keys
            subNode = node.map[char]
            if(subNode != None):
                node = subNode        
        return node.getOptions()


class Node:
    # arr is the array of options that are valid for this path
    # context is the path already built.
    def __init__(self, arr, context):
        self.value = arr
        self.context = context
        self.map = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f':
                    None, 'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None, 'm': None, 'n': None, 'o': None, 'p': None, 'q': None, 'r': None, 's': None, 't': None, 'u': None, 'v': None, 'w': None, 'x': None, 'y': None, 'z': None, }

    def add(self, item):
        # assuming items are all valid
        self.value.append(item)

    def getOptions(self):
        return self.value

    def distribute(self):
        # l is a the length of context, prevents errors later
        for i in self.value:
            if(len(i) > self.context):
                character = i[self.context]
                if(self.map[character] == None):
                    arr = []
                    arr.append(i)
                    self.map[character] = Node(arr, self.context + 1)
                else:
                    self.map[character].add(i)
        for i in self.map.values():
            if(i != None):
                i.distribute()
        
            

tree = AutoCompleteTree(["dog", "deer", "deal", "array"])
# s = '{ '
# for i in range (1, 27):
#     char = chr(64 + i)
#     s += "'%s': None, " % (char.lower())
# s += '}'    
# print(s)
print(tree.getAutoComplete('dea'))

