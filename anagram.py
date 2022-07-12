# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
    # [assignment] Add your code here

    if(sorted(word1) == sorted(word2)):
        print(sorted(word1), sorted(word2))
        return True
    return False

print(find_anagram("listen", "silent"))


#submitted by Adedolapo Olutuyo I4G000435EAL

#This is just for practice.

