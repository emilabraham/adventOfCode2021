# Find all paths through the cave
# First step is to create a Cave object: Cave(value, isSmall, connections)
# Second step is to create a dictionary of each cave's connections { Cave.value: list(Cave)}
# Final step is to create a list of all paths through the cave
# How do I figure out when I've tried all possible paths?
# I think recursion might be the way to go?
fp = open("input2")
lines = fp.readlines()
cavernMap = {}

# Represents a cave
class Cave:
    def __init__(self, value, isSmall, connections):
        self.value = value
        self.isSmall = isSmall
        self.connections = connections # List of strings which are the keys in the dictionary
    
    def printMe(self):
        print("Value: " + str(self.value) + " isSmall: " + str(self.isSmall) + " connections: " + str(self.connections))

def printCaveMap(cavernMap):
    for key in cavernMap:
        cavernMap[key].printMe()

# Remove newline character from a string
def removeNewLine(s):
    return s.replace('\n', '')

# Create a Cave for each line in the input file
def createCave(line):
    splitLine = line.split('-')
    entrance = splitLine[0]
    exit = splitLine[1]
    isSmall = entrance.islower()
    return Cave(entrance, isSmall, [exit])

# Build a map of caves and their connections
# TODO: I need to reverse the cave path list so that we have keys for the exits as well.
# TODO: This way we have a complete map.
def createCavernMap(cavernMap, lines):
    for line in lines:
        cave = createCave(removeNewLine(line))
        endPath = cave.connections[0]
        if (cave.value in cavernMap or endPath in cavernMap):
            if (cave.value in cavernMap):
                existingCave = cavernMap[cave.value]
                existingCave.connections.append(cave.connections[0])
                cavernMap[cave.value] = existingCave
            if (endPath in cavernMap):
                existingCave = cavernMap[endPath]
                existingCave.connections.append(cave.value)
                cavernMap[endPath] = existingCave
        else:
            cavernMap[cave.value] = cave

createCavernMap(cavernMap, lines)
printCaveMap(cavernMap)
