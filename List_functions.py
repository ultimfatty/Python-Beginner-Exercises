def name_function():
    userName = input ("What is your name?\n")
    return userName
# length = len(userName)
# print(userName, "is the best \nLength of the name is", length)

# cars = ["Ford", "Volvo", "BMW"]
# cars.append("Mercedes")

# for x in cars:
#     print(x)
def array_function(userName):
    wordArray = []
    for i in userName:   
        wordArray.append(i)
    return wordArray
    
# print(wordArray)
def reverse_array(wordArray):
    flip = wordArray
    flip = wordArray.reverse()
    print(wordArray)
    return flip

userName = name_function()
wordArray = array_function(userName)
# reverse_array(wordArray)

def count_num_chars(wordArray):
    count_Arr = []
    i = 0
    for x in wordArray:
        for y in wordArray:
            if y==wordArray[0]:
                i = 1
            if x==y & y!=read.index(i-1):
                i = i+1
                read = read.append()
                count_Arr.append(i) 
    j = 0
    k = 0
    read = []
    while i<len(count_Arr)-1:
        while j<len(count_Arr)-1:
            if count_Arr.index(i) == count_Arr.index(j)
                read == read.append()
                while k<len(read)-1
                    if read(k)!=countArr.index(i)
                    k+=1
            j+=1
        i+=1               

    print(count_Arr) 
                
count_num_chars(wordArray)                 

