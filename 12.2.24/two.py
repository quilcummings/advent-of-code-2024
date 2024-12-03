rows = []
output = []
failIndexes = []


def readFile():
    with open('two-input') as my_file:
        for line in my_file:
            line = line.strip()
            line = line.split()
            line = [int(l) for l in line]
            
            rows.append(line)

def checkAsc(row):
    rev = row[::-1]
    
    if sorted(row) == row or sorted(rev) == rev:
        return True
    else:
        return False

def checkDiffs(row):
    for x in range(len(row)-1):
        if abs(int(row[x]) - int(row[x+1])) > 3 or row[x] == row[x+1]:
            return False
    return True

def removeEach(row):
    for x in range(len(row)):
        hold = row[x]
        ind = x
        row.pop(x)

        print(row)
        if (checkAsc(row) and checkDiffs(row)):
            return True
            
        row.insert(ind, hold)
        print(row)

    return False

def main():
    readFile()
    safeCount = 0

    for x in range(len(rows)):
        if (checkAsc(rows[x]) and checkDiffs(rows[x])):
            safeCount+=1
        else:
            failIndexes.append(x)

    print(safeCount)

def main2():
    readFile()
    safeCount = 0

    for row in rows:
        if removeEach(row):
            safeCount+=1

    print(safeCount)
            
main2()

        