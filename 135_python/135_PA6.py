# Note: Python does not have macros
import os.path

def getWords():
    word_string = f.read().replace("\n", "")
    new_string = word_string.replace(".", " ")
    words_array = new_string.split(" ")
    words_array.pop()
    count = 0
    for x in words_array:
        count += 1
    return words_array, count

def countLetters():
    lcount = 0
    for x in words:
        for i in x:
            if i.isalpha():
                lcount += 1
    return lcount

def countLowerCase():
    lowCount = 0
    for x in words:
        for i in x:
            if i.islower():
                lowCount += 1
    return lowCount

def countVowels():
    vcount = 0
    for x in words:
        for i in x:
            if i.lower() in ("a", "e", "i", "o", "u"):
                vcount += 1
            elif i.upper() in ("A", "E", "I", "O", "U"):
                vcount += 1
    return vcount

name = "poem.txt"
if os.path.exists(name):
    f = open(name, "r")
    results = getWords()
    words = results[0]
    num_words = results[1]
    f.close()
    num_letters = countLetters()
    print("Number of letters: " + str(num_letters))
    num_lowercase = countLowerCase()
    print("Number of lowercase: " + str(num_lowercase))
    num_vowels = countVowels()
    print("Number of vowels: " + str(num_vowels))
else:
    print(f"The file {name} does not exist. ")
