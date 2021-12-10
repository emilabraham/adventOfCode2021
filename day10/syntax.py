# Find corrupted and incomplete syntax
fp = open("input")
lines = fp.readlines()
openStack = []
openCharacters = ["(", "[", "{", "<"]
closeCharacters = [")", "]", "}", ">"]
syntaxScore = {")": 3, "]": 57, "}": 1197, ">": 25137}

# Remove newline character from a string
def removeNewLine(s):
    return s.replace('\n', '')

lines = list(map(removeNewLine, lines))

# Calculate the score of the syntax error
def calculateSyntaxErrorScore(char):
    return syntaxScore[char]

# Match up the open and close characters
# For now, this will just print out the errors
def match(line):
    for char in line:
        if char in openCharacters:
            openStack.append(char)
        elif char in closeCharacters:
            if len(openStack) == 0:
                print("Corrupt line with wrong close character: " + char)
            else:
                openChar = openStack.pop()
                # print("Trying to close " + openChar + " with " + char)
                expectedClose = closeCharacters[openCharacters.index(openChar)]
                if openChar != openCharacters[closeCharacters.index(char)]:
                    print("Expected " + expectedClose + " but found " + char + " instead")
                    return calculateSyntaxErrorScore(char)
                # else: 
                #     print("Correctly closed " + openChar + " with " + char)
    
    if len(openStack) != 0:
        print("Incomplete line")
    return 0

# Sum the scores of all the lines
def calculateTotalScore(lines):
    totalScore = 0
    for line in lines:
        totalScore += match(line)
    return totalScore

print(calculateTotalScore(lines))
