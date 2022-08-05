from turtle import st
# Finding and replacing all chars besides the first with $ sign

def input_func():
    print("Type a word")
    str = input()
    return str

def dollar_char(str):
    char_1 = str[0]
    i = 0
    wordArray = []
    new_str = ""

    for letters in str:
        if letters == str[0] and i != 0:
            wordArray.append("$")
            print(wordArray)
        else: 
            wordArray.append(letters)
        i+=1

    for characters in wordArray:
        new_str += characters

    print(new_str)
    return new_str

str = input_func()
new_str = dollar_char(str)