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

# START SOLUTION #

import os
import time
# Object that contains the tree structure and methods that
# enable a user to query said structure.
class AutoCompleter:
    # Dictionary is the entire array / list of words that are to be considered
    def __init__(self, dictionary):
        self.dictionary = dictionary
        # root to the data structure that contains all options
        self.root = DictionaryNode(self.dictionary, 0)
        # populates the branches of each tree
        self.root.build()
    
    # Method that returns all autocomplete options based on the dictionary
    # tree and the string provided.
    def getAutoComplete(self, str):
        # Empty array that might be overwritten if values are found.
        arr = []
        # The current node being explored. Always starts from the root.
        # Is either set to a child of itself or none after every iteration
        # of the loop.
        node = self.root
        # Iterates over every character in the provided string
        for char in str.lower():
            # checks if the char is a valid key on the current node
            if(char in node.map.keys()):
                # in the case it is
                ## set the current node to the value linked with that key.
                ### No Null check is required as keys are only added if a 
                ### valid entry is in the list.
                ### If the key is there, there will be a node.
                node = node.map[char]
            else:
                # in the case it isn't
                ## set the current to null and break the loop
                ## as we've reached the end of path and no words 
                ## in the dictionary matched the provided string.
                node = None
                break
        # Simple null check to see if we found a valid node
        if(node != None):
            # in the case we did
            ## set 'arr' to the options of the current node.
            arr = node.getOptions()  
        # regardless, we return arr.      
        return arr


class DictionaryNode:
    # arr is the array of options that are valid for this path
    # Index is the length of string being considered. 
    ## The value is always equal to it's parent's index + 1
    def __init__(self, arr, index):
        self.options = arr
        self.index = index
        self.map = {}

    def add(self, item):
        # assuming items are all valid
        self.options.append(item)

    def getOptions(self):
        return self.options

    def build(self):
        # Iterates over every element in the node's options.
        for i in self.options:
            # checks if the string is longer than the value of this node's 
            # index. Prevents Out_Of_Index_Exceptions
            if(len(i) > self.index):
                # Grabs the lowercase value of the character at the
                # position of self.index
                character = i[self.index].lower()
                # Checks if the character is not a valid entry in
                # this node's map.
                if(character not in self.map.keys()):
                    # In the case it is 
                    ## we create an empty array and append the word 
                    # to it.
                    arr = []
                    arr.append(i)
                    ## we then create a new node and initialize it with
                    ## the new array as well as the incremented index.
                    ## lastly, we map this node to key of 'character'
                    self.map[character] = DictionaryNode(arr, self.index + 1)
                else:
                    # In the case it isn't:
                    ## We know there's already a Node for the letter,
                    ## so we just append the word to it's options.
                    self.map[character].add(i)
        # Lastly, we iterate through every value in the map 
        for i in self.map.values():
            # We check if it isn't null
            if(i != None):
                # in the case it isn't:
                ## We call the build() method to evaluate this node and
                ## all of it's potential children.
                i.build()

# END SOLUTION #

# START TESTING #

def printOptions(options):
    s = ''
    for option in options:
        if(len(s) + len(option) >= 2 ** 14):    
            print(s.strip())
            s = "%s\n" % (option)
        else:
            s += "%s\n" % (option)
    print(s.strip())
    print('Found %s autocomplete options.' % (len(options)))

# Stores the time the program started, used for stats.
t = time.time()
print("Loading list of words from file.")
# Opens a list of words from a file.
listFile = open('Problem 11/words.txt', 'r')
# Creates an empty array that we can append words to
list = []
# Iterates over every line in document
for line in listFile:
    # Strips the line to remove unnecessary characters.
    line = line.strip() 
    # Appends the line / word to the list.
    list.append(line)
# Closes the file for good merits.
listFile.close()
# Stores the time the method finished. Used to calc. how long it took.
t2 = time.time()
l = len(list)
print('Finished loading list of %s word(s). Took %s seconds' % (l, t2 - t))
t = time.time()
print("Building tree from list.")
# Builds the AutoCompleter / DictionaryTree from the list
tree = AutoCompleter(list)
t2 = time.time()
print('Finished building list of words. Took %s seconds' % (t2 - t))

# Loops around user input
inp = input("Enter a piece of text: ")
while(inp != ""):
    # Queries the AutoCompleter from the input
    options = tree.getAutoComplete(inp)
    # Prints options to screen
    printOptions(options)
    inp = input("Enter a piece of text: ")
# END TESTING #
