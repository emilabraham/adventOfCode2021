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
    pairs = []
    for rule in rules:
        rule = removeNewLine(rule)
        rule = rule.split(" -> ")
        pairs.append(Pair(list(rule[0]), rule[1]))
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
            
rules = parseRules(rules)
template = insertIntoTemplateNTimes(template, rules, 10)
count = elementCounts(template)
print(count)
print(countDifference(count))