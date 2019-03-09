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

import os
import time

class AutoCompleteTree:
    def __init__(self, arr):
        self.arr = arr
        self.root = Node(self.arr, 0)
        self.root.distribute()
    
    def getArr(self):
        return self.arr

    def getAutoComplete(self, str):
        arr = []
        node = self.root
        for char in str:
            # assuming all characters are valid keys
            subNode = node.map[char]
            if(subNode != None):
                node = subNode
            else:
                node = None
                break
        if(node != None):
            arr = node.getOptions()        
        return arr


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
                character = i[self.context].lower()
                if(self.map[character] == None):
                    arr = []
                    arr.append(i)
                    self.map[character] = Node(arr, self.context + 1)
                else:
                    self.map[character].add(i)
        for i in self.map.values():
            if(i != None):
                i.distribute()


t = time.time()
print("Loading list of words from file.")
listFile = open('Problem 11/words.txt', 'r')
list = []
for line in listFile:
    line = line.strip()  
    valid = True
    for char in line:
        char = char.lower()
        if char not in 'abcdefghijklmnopqrstuvwxyz':
            valid = False
            break
    if(valid):
        list.append(line)
t2 = time.time()
l = len(list)
print('Finished loading list of %s word(s). Took %s seconds' % (l, t2 - t))
t = time.time()
print("Building tree from list.")
tree = AutoCompleteTree(list)
t2 = time.time()
print('Finished building list of words. Took %s seconds' % (t2 - t))

user = input("Enter a piece of text: ")
while(user != ""):
    options = tree.getAutoComplete(user)
    print(options)
    user = input("Enter a piece of text: ")
