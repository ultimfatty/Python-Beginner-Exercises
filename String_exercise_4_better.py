# Finding and replacing all chars besides the first with $ sign

def input_func():
    print("Type a word")
    str = input()
    return str

def dollar_char(str):  
    char_1 = str[0]
    str = str.replace(char_1, '$')
    str = char_1 + str[1:]
    print(str)

str = input_func()
dollar_char(str)