# Pair insertion into a polymer template
fp = open("input2")
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

rules = parseRules(rules)
printRules(rules)
