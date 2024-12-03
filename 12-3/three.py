import re

input = []
output = []

new_input = []


def readFile():
    with open('12-3/three-input.txt') as file:
        #text = file.read()
        for line in file:
            input.append(line)

    with open("12-3/three-input.txt", "r") as filey:
        text = filey.read()

    new_input.append(text)

def findEquations(line):
    equations = re.findall(r"mul[(]\d+,\d+[)]", line, flags=re.DOTALL)

    for e in equations:
        e = re.sub(r"mul\(|\)", "", e)

        nums = e.split(",")
        nums = [int(n) for n in nums]

        output.append(nums[0]*nums[1])

def findSwitches(input):
    dos = re.findall(r"don't\(\).+?do\(\)", input, flags=re.DOTALL)
    removed = re.sub(r"don't\(\).+?do\(\)", "", input, flags=re.DOTALL)

    findEquations(removed)

def main():
    readFile()
    for i in input:
        findEquations(i)

    sum = 0
    for num in output:
        sum+=num
    print(sum)

def main2():
    readFile()
    findSwitches(new_input[0])

    sum = 0
    for num in output:
        sum+=num
    print(sum)

main2()
