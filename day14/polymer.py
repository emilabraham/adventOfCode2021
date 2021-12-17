import math
# Pair insertion into a polymer template
fp = open("input")
lines = fp.readlines()
template = lines[0]
rules = lines[2:]

# Represents a polymer insertion rule
class Pair:
    def __init__(self, pairing, insertion):
        self.pairing = pairing
        self.insertion = insertion

    def printMe(self):
        return (str(self.pairing) + " -> " + str(self.insertion))

# Remove the new line character from the input
def removeNewLine(s):
    return s.replace('\n', '')

template = list(removeNewLine(template))

# Parse the input into rules
def parseRules(rules):
    pairs = {}
    for rule in rules:
        rule = removeNewLine(rule)
        rule = rule.split(" -> ")
        pairs[rule[0]] = rule[1]
    return pairs

# Print the rules
def printRules(rules):
    for rule in rules:
        print(rule.printMe())

# One iteration of polymer pair insertion
def insertIntoTemplate(template, rules):
    newTemplate = []
    for i in range(len(template)):
        pairing = template[i:i+2]
        added = False
        for rule in rules:
            if (rule.pairing == pairing):
                added = True
                newTemplate += pairing[0] + rule.insertion
        if not added:
            newTemplate += pairing[0]
    
    return newTemplate

# Insert into the template n times
# Too slow. Deprecate this in favor on keep track of counts instead
def insertIntoTemplateNTimes(template, rules, n):
    for i in range(n):
        template = insertIntoTemplate(template, rules)
    return template

# Return a dictionary of the counts of each element
def elementCounts(template):
    counts = {}
    for element in template:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

# Return difference of largeetst and smallest counts
def countDifference(counts):
    largetsCount = 0
    smallestCount = 0
    for element in counts:
        if counts[element] > largetsCount:
            largetsCount = counts[element]
        if counts[element] < smallestCount or smallestCount == 0:
            smallestCount = counts[element]
    
    return largetsCount - smallestCount

# Convert into a count of the different types of pairs
def convertToDictionary(template):
    counts = {}
    for i in range(len(template) - 1):
        if template[i]+template[i+1] in counts:
            counts[template[i]+template[i+1]] += 1
        else:
            counts[template[i]+template[i+1]] = 1

    return counts

# Update the counts of each pairing based on rules.
def oneInsertion(counts, rules):
    countCopy = counts.copy()
    for k in counts.keys():
        insertionCharacter = rules[k]
        key1 = k[0] + insertionCharacter
        key2 = insertionCharacter + k[1]
        quantity = counts[k]
        countCopy[k] -= quantity
        if key1 in countCopy:
            countCopy[key1] += quantity
        else:
            countCopy[key1] = quantity
        if key2 in countCopy:
            countCopy[key2] += quantity
        else:
            countCopy[key2] = quantity

    return countCopy

# insert into the template n times
def insertIntoTemplateNTimes(counts, rules, n):
    for i in range(n):
        counts = oneInsertion(counts, rules)
    return counts

# Given a dictionary of pairs, count the occurrences of each element
def countOccurrences(counts, template):
    characterCount = {}
    for k in counts.keys():
        key1 = k[0]
        key2 = k[1]
        characterCount[key1] = 0
        characterCount[key2] = 0

    for k in characterCount.keys():
        intermediateCount = 0
        for k2 in counts.keys():
            if k == k2[0] and counts[k2] > 0:
                intermediateCount += counts[k2]
            if k == k2[1] and counts[k2] > 0:
                intermediateCount += counts[k2]
        characterCount[k] = intermediateCount
        characterCount[k] = math.ceil(intermediateCount/2)

    return characterCount
            
rules = parseRules(rules)
count = convertToDictionary(template)
count = insertIntoTemplateNTimes(count, rules, 40)
# print(count)
characterCount = countOccurrences(count, template)
# print(characterCount)
diff = countDifference(characterCount)
print(diff)