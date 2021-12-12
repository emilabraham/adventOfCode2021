# Simulate octopus flashes
fp = open("input2")
lines = fp.readlines()
grid = []

# Represents a point with an x and y coordinate.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printMe(self):
        return (str(self.x) + "," + str(self.y))

# Remove newline character from a string
def removeNewLine(s):
    return s.replace('\n', '')

# Create the grid from the input
def createGrid(grid, lines):
    grid = []
    for line in lines:
        line = removeNewLine(line)
        line = [x for x in line]
        grid.append(list(map(int, line)))

createGrid(grid, lines)
print(lines)
print(grid)