# Find corrupted and incomplete syntax
fp = open("input")
lines = fp.readlines()
openStack = []
openCharacters = ["(", "[", "{", "<"]
closeCharacters = [")", "]", "}", ">"]
syntaxScore = {")": 3, "]": 57, "}": 1197, ">": 25137}
completionScore = {")": 1, "]": 2, "}": 3, ">": 4}

# Remove newline character from a string
def removeNewLine(s):
    return s.replace('\n', '')

lines = list(map(removeNewLine, lines))

# Calculate the score of the syntax error
def calculateSyntaxErrorScore(char):
    return syntaxScore[char]

# Calculate the score of autocompleting the open characters
def calculateAutocompleteScore(openStack):
    completionStack = []
    for char in openStack:
        completionStack.append(closeCharacters[openCharacters.index(char)])
    completionStack.reverse()
    totalScore = 0
    for char in completionStack:
        totalScore *= 5
        totalScore += completionScore[char]
    openStack.clear()
    return totalScore

# Match up the open and close characters
# For now, this will just print out the errors
def match(line, autocomplete=False):
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
                    openStack.clear()
                    return calculateSyntaxErrorScore(char)
                # else: 
                #     print("Correctly closed " + openChar + " with " + char)
    
    if len(openStack) != 0:
        print("Incomplete line. Here's what's left open: ", end='')
        print(openStack)
        if autocomplete:
            return calculateAutocompleteScore(openStack)
    openStack.clear()
    return 0

# Sum the scores of all the lines
def calculateTotalScore(lines):
    totalScore = 0
    for line in lines:
        totalScore += match(line)
    return totalScore

# Find all the incomplete lines.
# Calculate their scores.
# Sort them, then find the middle one.
def onlyAutocompleteScore(lines):
    incompleteLines = list(filter(lambda line: match(line) == 0, lines))
    autocompleteScores = list(map(lambda line: match(line, True), incompleteLines))
    autocompleteScores.sort()
    return autocompleteScores[len(autocompleteScores)//2] # Floor division. Didn't know this was a thing. Thanks github copilot.

# print(calculateTotalScore(lines))
print(onlyAutocompleteScore(lines))
