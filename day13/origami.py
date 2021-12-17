# Fold the transparent paper and align the dots
fp = open("input")
lines = fp.readlines()
coordinates = []
folds = []

# Represents a point with an x and y coordinate.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printMe(self):
        return (str(self.x) + "," + str(self.y))# Remove newline character from a string

# Represents a fold
class Fold:
    def __init__(self, axis, direction):
        self.axis = axis
        self.direction = direction

    def printMe(self):
        return (str(self.axis) + "," + str(self.direction))

def removeNewLine(s):
    return s.replace('\n', '')

# Parse the input into coordinates and folds
parsingCoordinates = True
for line in lines:
    line = removeNewLine(line)
    if len(line) == 0:
        parsingCoordinates = False
    if len(line) > 0 and parsingCoordinates:
        coordinates.append(line)
    if len(line) > 0 and not parsingCoordinates:
        folds.append(line)

# Create a list of points from the coordinates
def convertToPoints(coordinates):
    points = []
    for coordinate in coordinates:
        x = int(coordinate.split(",")[0])
        y = int(coordinate.split(",")[1])
        points.append(Point(x, y))
    return points

# Convert the input into folds
def convertToFolds(folds):
    newFolds = []
    for fold in folds:
        fold = fold.split(" ")[2]
        fold = fold.split("=")
        fold = Fold(int(fold[1]), fold[0])
        newFolds.append(fold)
    return newFolds

# Find the largest x and y coordinate
def findLargestValue(points):
    largestValues= [0, 0]
    for point in points:
        if point.x > largestValues[0]:
            largestValues[0] = point.x
        if point.y > largestValues[1]:
            largestValues[1] = point.y
    return largestValues

# Create a grid from the coordinates
def createGrid(points, largestValues):
    grid = []
    for y in range(0, largestValues[1] + 1):
        grid.append([])
        for x in range(0, largestValues[0] + 1):
            grid[y].append(".")
    for point in points:
        grid[point.y][point.x] = "#"
    return grid

# Print the grid nicely
def printGrid(grid):
    for row in grid:
        for column in row:
            print(column, end="")
        print()

# Perform a horizontal fold along axis
def performYFold(grid, axis):
    index = 1
    for y in range(axis + 1, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "#":
                grid[axis-index][x] = "#"
        index += 1

    grid = grid[:axis]
    return grid

# Perform a horizontal fold along axis
def performXFold(grid, axis):
    index = 1
    for y in range(0, len(grid)):
        for x in range(axis + 1, len(grid[y])):
            if grid[y][x] == "#":
                grid[y][axis-index] = "#"
            index += 1
        index = 1

    for (i, row) in enumerate(grid):
        grid[i] = row[:axis]

    return grid

# Count the number of dots in the grid
def countDots(grid):
    count = 0
    for row in grid:
        for column in row:
            if column == "#":
                count += 1
    print(count)

# Peform the folds on the grid
def performFolds(grid, folds):
    for fold in folds:
        if fold.direction =="y":
            grid = performYFold(grid, fold.axis)
        if fold.direction =="x":
            grid = performXFold(grid, fold.axis)

    return grid

coordinates = convertToPoints(coordinates)
largetsValues = findLargestValue(coordinates)
grid = createGrid(coordinates, largetsValues)
# grid = performYFold(grid, 7)
grid = performXFold(grid, 655)
countDots(grid)
folds = convertToFolds(folds)
printGrid(performFolds(grid, folds))