# Write a function that given a string of characters, returns the longest word in the sentence.


def longest_Word(sentence):
    longestWord = ""
    if " " not in sentence:
        return sentence
    else:
        split = sentence.split(" ")
        print(split)
        for word in split:
            if(len(word) > len(longestWord)):
                longestWord = word
        return longestWord


print(longest_Word("Not so long sentence."))
