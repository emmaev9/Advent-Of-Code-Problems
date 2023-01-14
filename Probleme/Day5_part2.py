def findNiceWord(word):
    cond1 = False
    cond2 = False
      
    for i in range(len(word)-1):
        dup = word[i:i+2]
        if dup in word[i+2:]:
            cond1 = True
    
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            cond2 = True

    if cond2 == True and cond1 == True:
            return True
    return False


countNiceWords = 0

with open("input5.txt", "r") as file:
    for word in file.readlines():
       # print(word)
        if findNiceWord(word):
            countNiceWords +=1
print(countNiceWords)
print(findNiceWord("xxyxx"))