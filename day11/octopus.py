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

def printGrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end="")
        print()

# Create the grid from the input
def createGrid(grid, lines):
    for line in lines:
        line = removeNewLine(line)
        line = [x for x in line]
        grid.append(list(map(int, line)))

# Given an point, find the adjacent points
def findAdjacents(grid, x, y):
    if y == 0: # Top row
        if x == 0: # Top left
            return [Point(x+1, y), Point(x, y+1), Point(x+1, y+1)]
        elif x == len(grid[y]) - 1: # Top right
            return [Point(x-1, y), Point(x, y+1), Point(x-1, y+1)]
        else:
            return [Point(x-1, y), Point(x, y+1), Point(x+1, y+1), Point(x-1, y+1), Point(x+1, y)]
    elif y == len(grid) - 1: # Bottom row
        if x == 0: # Bottom left
            return [Point(x+1, y), Point(x, y-1), Point(x+1, y-1)]
        elif x == len(grid[y]) - 1:
            return [Point(x-1, y), Point(x, y-1), Point(x-1, y-1)]
        else:
            return [Point(x-1, y), Point(x, y-1), Point(x+1, y-1), Point(x-1, y-1), Point(x+1, y)]
    elif x == 0: # left column
        return [Point(x+1, y), Point(x, y-1), Point(x, y+1), Point(x+1, y-1), Point(x+1, y+1)]
    elif x == len(grid[y]) - 1: # right column
        return [Point(x-1, y), Point(x, y-1), Point(x, y+1), Point(x-1, y-1), Point(x-1, y+1)]
    else:
        return [Point(x-1, y), Point(x, y-1), Point(x, y+1), Point(x-1, y-1), Point(x-1, y+1), Point(x+1, y-1), Point(x+1, y+1)]

# A flash iteration
# If the energy exceeds 9, then increase the energy of adjacent cells by 1.
# Do this by appending them all to a list and then iterating through that list.
# Keep track of the points that are flashing. They need to be reset to 0.
# An iteration is complete when the adjacents list is complete.
def flashIteration(grid, adjacents, flashed):
    while (len(adjacents) > 0):
        point = adjacents.pop()
        if (grid[point.y][point.x] == 9):
            flashed.append(point)
            pointAdjacents = findAdjacents(grid, point.x, point.y)
            pointAdjacents = list(filter(lambda p: notInList(p, flashed), pointAdjacents))
            adjacents += pointAdjacents
        else:
            grid[point.y][point.x] += 1
    for point in flashed:
        grid[point.y][point.x] = 0

def printPoints(points):
    for point in points:
        print(point.printMe())

# Return true if the point is not in the list
def notInList(point, points):
    for p in points:
        if p.x == point.x and p.y == point.y:
            return False
    return True

# Calculate the energies per iteration.
# At each iteration it will also handle the flashes.
# Return the total number of flashes.
def calculateEnergies(grid, iterations):
    flashed = []
    adjacents = []
    flashCount = 0
    for i in range(iterations):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 9 and notInList(Point(x, y), flashed):
                    flashed.append(Point(x, y))
                    pointAdjacents = findAdjacents(grid, x, y)
                    pointAdjacents = list(filter(lambda p: notInList(p, flashed), pointAdjacents))
                    adjacents += pointAdjacents
                    flashIteration(grid, adjacents, flashed)
                else:
                    grid[y][x] += 1
        print(len(flashed))
        printPoints(flashed)
    return flashCount

createGrid(grid, lines)
calculateEnergies(grid, 2)
printGrid(grid)