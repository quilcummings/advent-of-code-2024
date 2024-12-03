colone = []
coltwo = []
output = []

def readFile():
    input = open('one-input-part1','r')

    line = input.readline()
    total = input.read()

    with open('one-input-part1') as my_file:
        for line in my_file:
            line = line.strip()
            line = line.split()
            colone.append(line[0])
            coltwo.append(line[1])

def sort(col):
    col.sort()

def difference(one, two, outarr):
    num = int(one) - int(two)
    outarr.append(abs(num))

def simularity(one, arrtwo, outarr):
    num = 0
    for x in arrtwo:  
        if int(x) == int(one):
            num+=1
            
        print(num)

    val = int(num)*int(one)
    outarr.append(val)
             
def main():
    readFile()

    sort(colone)
    sort(coltwo)
    print(colone)
    print(coltwo)

    sum = 0
    for i in range(len(colone)):
        difference(colone[i], coltwo[i], output)
        
    for x in output:
        sum+=x

    print(output)
    print(sum)


def main2():
    readFile()

    print(colone)
    print(coltwo)

    sum = 0

    for i in range(len(colone)):
        simularity(colone[i], coltwo, output)

    for x in output:
        sum+=x

    print(output)
    print(sum)

main2()






