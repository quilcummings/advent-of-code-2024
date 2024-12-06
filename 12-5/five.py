input = []

rules = []
updates = []
mids = []

def readFile():
    with open('12-5/five-input.txt') as file:
        for line in file:
            input.append(line.strip())

def breakDown(input):
    for line in input:
        if "|" not in line:
            if line != "":
                updates.append(line.split(","))
                
        else:
            rule = line.split("|")
            rules.append(rule)

def checkRules(update, ind):
    for j in range (len(rules)):
        if rules[j][0] == update[ind]:
            if rules[j][1] == update[ind+1]:
                return True
            
    return False

def getMiddle(update):
    mid = int(len(update)/2)
    return(update[mid])


def main():
    readFile()
    breakDown(input)

    for x in range(len(updates)):
        count = 1
        for y in range(len(updates[x])-1):
            if checkRules(updates[x], y): 
                count+=1
            
        if count == len(updates[x]):
            mids.append(getMiddle(updates[x]))
            print("Middle: " + str(getMiddle(updates[x])))
        else:
            print("Fail: " + str(updates[x]))

    sum = 0       
    for num in mids:
        sum+=int(num)

    print(sum)
    
main()