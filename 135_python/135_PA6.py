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


def countLetters():
    pass

def countLowerCase():
    pass

def countVowels():
    pass

name = "poem.txt"
if os.path.exists(name):
    f = open(name, "r")
    getWords()
    f.close()
else:
    print(f"The file {name} does not exist. ")
