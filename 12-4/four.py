input = []

def readFile():
    with open('12-4/four-input.txt') as file:
        for line in file:
            input.append(line.strip())


def checkAdj(tileX, tileY, str, ind, dx, dy):
    if ind == 3:
        return True
    
    if tileX < 0 or tileX >= len(input) or tileY < 0 or tileY >= len(input[0]):
        return False


    if input[tileX][tileY] == str[ind]:
        return checkAdj(tileX + dx, tileY + dy, str, ind + 1, dx, dy)
    return False


def isCenter(x, y):
    if input[x][y] == "A":
        return True


def main():
    readFile()
    print(input)

    count = 0
    rows, cols = len(input), len(input[0])
    directions = [(1, 0),(1, 1),(0, 1),(-1, 1),(-1, 0),(-1, -1),(0, -1),(1, -1)]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if checkAdj(i, j, "XMAS", 0, dx, dy):
                    count += 1
                    print(input[i][j])
                    print(str(i) + ", " + str(j))

    print(count)

def main2():
    readFile()
    print(input)

    count = 0
    rows, cols = len(input), len(input[0])
    directions = [(-1, 1),(-1, -1),(1, 1),(1, -1)]

    for i in range(rows):
        for j in range(cols):
            
                # if checkAdj(i, j, "MAS", 0, -1, 1) & checkAdj(i, j, "MAS", 0, 1, -1):
                #     if checkAdj(i, j, "MAS", 0, -1, -1) & checkAdj(i, j, "MAS", 0, 1, 1):
                #         count+=1
                #         print(input[i][j])
                #         print(str(i) + ", " + str(j))

            for dx, dy in directions:
                if checkAdj(i, j, "MAS", 0, dx, dy):
                    count += 1
                    print(input[i][j])
                    print(str(i) + ", " + str(j))

    print(count)

main2()