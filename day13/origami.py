# Fold the transparent paper and align the dots
fp = open("input2")
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

def printGrid(grid):
    for row in grid:
        for column in row:
            print(column, end="")
        print()

coordinates = convertToPoints(coordinates)
largetsValues = findLargestValue(coordinates)
grid = createGrid(coordinates, largetsValues)
printGrid(grid)