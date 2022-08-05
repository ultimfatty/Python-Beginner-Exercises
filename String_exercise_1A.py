def input_function():
    print("Type a word")
    input_string = input()
    result = f'"{input_string}"'
    print("string 1 =",result)
    return input_string

def first_middle_last(input_string):
    # i = 0
    # output = []
    # for letter in input_string:
    #     if i == 0: 
    #         output.append(letter)
    #     elif i == (len(input_string)-1)/2:
    #         output.append(letter)
    #         # print(output)
    #     elif i == len(input_string)-1:
    #         output.append(letter)
    #     i+=1
    first_letter = input_string[0]
    middle_index = int(len(input_string)/2)
    middle_letter = input_string[middle_index]
    last_letter = input_string[len(input_string)-1]

    outputA = first_letter + middle_letter + last_letter
    print(outputA)
    
    return outputA

def middle_three(input_string):
    str = input_string
    middle_index = int(len(str)/2)
    middle_left = middle_index - 1
    middle_right = middle_index + 1
    outputB = str[middle_left:middle_right+1]
    print(outputB)
    print(str[middle_right])
    return outputB

input_string = input_function()
# first_middle_last(input_string)
middle_three(input_string)