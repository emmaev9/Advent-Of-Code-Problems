def findArea(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l

def find2Min(l,w, h):
    min1 = min(l,w,h)
    min2 =0
    if min1 ==l:
        if w < h:
            min2 = w
        else:
            min2 = h
    if min1 ==w:
        if l < h:
            min2 = l
        else:
            min2 = h
    if min1 ==h:
        if w < l:
            min2 = w
        else:
            min2 = l
    #return min1 * min2 #pentru partea 1
    return 2*min1 + 2*min2 
    

def calculatePaper():
    sum = 0
    
    with open("input2.txt", "r") as ext_file:
        for line in ext_file:
            data = line.strip().split('x')
            l = int(data[0])
            w = int(data[1])
            h = int(data[2]) 
            sum = sum + findArea(l,w,h) + find2Min(l,h,w)
    return sum

def calculateRibbon():
    sum = 0
    with open("input2.txt", "r") as ext_file:
        for line in ext_file:
            data = line.strip().split('x')
            l = int(data[0])
            w = int(data[1])
            h = int(data[2]) 
            sum = sum + l*w*h + find2Min(l,h,w)
    return sum


#paperNeeded = calculatePaper()
#print("Paper:" + paperNeeded)
ribbonNeeded = calculateRibbon()
print(f"Ribbon: {ribbonNeeded}")