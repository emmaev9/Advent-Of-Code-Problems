from collections import Counter

def findNiceWord(word):
    cond1 = False
    cond2 = False
    cond3 = True
    vowel = set("aeiouAEIOU")
    countVowel = 0
    for letter in word:
        if letter in vowel:
            countVowel += 1

    if countVowel >= 3:
        cond1 = True

    countDups = 0    
    l = list(word)
    for i in range(0,len(l)-1):
        if l[i] == l[i+1]:
            countDups += 1
        if (l[i] == 'a' and l[i+1] == 'b') or (l[i] == 'c' and l[i+1]=='d') or (l[i] == 'p' and l[i+1] =='q') or (l[i] == 'x' and l[i+1] =='y'):
            cond3 = False
    if countDups >= 1:
        cond2 = True

    if cond3 == True:
        if cond2 == True and cond1 == True:
            return True
    return False
   

countNiceWords = 0

with open("input5.txt", "r") as file:
    for word in file.readlines():
        if findNiceWord(word):
            countNiceWords +=1
print(countNiceWords)