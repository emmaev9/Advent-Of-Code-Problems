def delivery():  #partea 1
    with open("input3.txt") as file:
        data = file.readline()
    x = 0
    y = 0
    count = 0
    position = (x,y)
    santaMap = {}
    santaMap[(x,y)] =1
    for index in data:
        if index == ">":
            x += 1
        if index == "<":
            x -= 1
        if index == "v":
            y -= 1
        if index == "^":
            y += 1
        
        newPosition = (x,y)

        if (x,y) in santaMap:
            santaMap[(x,y)] +=1
        else:
            santaMap[(x,y)] =1
    return len(santaMap)


def santa_robosanta(): #partea 2
    with open("input3.txt") as file:
        data = file.readline()
    sx = 0
    sy = 0
    rx = 0
    ry = 0
    count = 0
    santaMap = {}
    santaMap[(sx,sy)] = 1
    santaMap[(rx,ry)] = 1
    move = 1
    for index in data:
        if move:
            if index == ">":
                sx += 1
            if index == "<":
                sx -= 1
            if index == "v":
                sy -= 1
            if index == "^":
                sy += 1
            if (sx,sy) in santaMap:
                santaMap[(sx,sy)] +=1
            else:
                santaMap[(sx,sy)] =1
            move = 0
        else:
            if index == ">":
                rx += 1
            if index == "<":
                rx -= 1
            if index == "v":
                ry -= 1
            if index == "^":
                ry += 1
            if (rx,ry) in santaMap:
                santaMap[(rx,ry)] +=1
            else:
                santaMap[(rx,ry)] =1
            move = 1
    return len(santaMap)


print("Part1: " + delivery())
print("Part2: " + santa_robosanta())

            
            
            


       



            
    


