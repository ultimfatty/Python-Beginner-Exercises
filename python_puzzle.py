def input_num():
    num_string = input()
    num_Array = []
    i = 0
    num = ""

    for char in num_string:
        if i != 0 and i != len(num_string)-1 and num_string[i] != ',' and num_string[i] != ",":
            num = num + char
        elif num_string[i] == ',' or i == len(num_string)-1:
            num = int(num)
            num_Array.append(num)
            num = ""
        i+=1
    print(num_Array)
    return num_Array

def check_num(num_Array):
    try:
        for integer in num_Array
            numValue = ord(num_Array)


# def nineteenth_occurrances():

num_Array = input_num()
