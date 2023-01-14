def controlLights(grid, instruction, r1,r2,r3,r4):
    
    for i in range(r1,r3+1):
        for j in range(r2, r4+1):
            if instruction == 'off':
                grid[i][j] = 0
            elif instruction == 'on':
                grid[i][j] = 1
            else:
                if grid[i][j] == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0

def fileRead():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for i in range(0,1000):
        for j in range(0,1000):
            grid[i][j] = 0

    for line in open("input6.txt" ,"r").readlines():
        data = line.replace(',', ' ').split()
        if data[0] == "turn":
            instruction = data[1]
            r1 = int(data[2])
            r2 = int(data[3])
            r3 = int(data[5])
            r4 = int(data[6])
        else:
            instruction = data[0]
            r1 = int(data[1])
            r2 = int(data[2])
            r3 = int(data[4])
            r4 = int(data[5])
        controlLights(grid, instruction, r1,r2,r3,r4)

    lightsOn = 0
    for i in range(0,1000):
        for j in range(0,1000):
            if grid[i][j] == 1:
                lightsOn += 1
    print(lightsOn)

fileRead()

