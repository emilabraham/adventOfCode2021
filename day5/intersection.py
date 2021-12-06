# Find the intersection of of lines.
fp = open("input")
lines = fp.readlines()
diagramSize = 1000
diagram = []

# Represents a point with an x and y coordinate.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def printMe(self):
        return (str(self.x) + "," + str(self.y))

# Represents a line with a start and end point.
class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
    
    def printMe(self):
        return self.start.printMe() + " -> " + self.end.printMe()

# Convert a string representation of a point into a Point object.
def convertToPoint(stringPoint):
    splitPoint = stringPoint.split(",")
    return Point(int(splitPoint[0]), int(splitPoint[1]))

# Convert a string representation of a line into a Line object.
def convertToLine(stringLine):
    splitLine = stringLine.replace('\n', '').split(" -> ")
    points = list(map(lambda point: convertToPoint(point), splitLine))
    line = Line(points[0], points[1])
    return line

# Filter out non-horizontal and non-vertical lines.
def onlyHorizontalOrVertical(line):
    if (line.start.x == line.end.x):
        return True
    elif (line.start.y == line.end.y):
        return True
    else:
        return False

# Converts a line into a list of points.
def convertToPoints(line):
    points = []
    if (line.start.x == line.end.x):
        for y in range(min(line.start.y, line.end.y), max(line.end.y, line.start.y) + 1):
            points.append(Point(line.start.x, y))
    elif (line.start.y == line.end.y):
        for x in range(min(line.start.x, line.end.x), max(line.end.x, line.start.x) + 1):
            points.append(Point(x, line.start.y))
    else:
        xValues = []
        yValues = []
        xIncrement = 1 if line.start.x < line.end.x else -1
        yIncrement = 1 if line.start.y < line.end.y else -1
        for x in range(line.start.x, line.end.x + xIncrement, xIncrement):
            xValues.append(x)
        for y in range(line.start.y, line.end.y + yIncrement, yIncrement):
            yValues.append(y)
        for i in range(0, len(xValues)):
            points.append(Point(xValues[i], yValues[i]))
    return points

def printDiagram():
    for y in range(0, diagramSize):
        for x in range(0, diagramSize):
            print(diagram[y][x], end=",")
        print("\n")

lines = list(map(convertToLine, lines))
# lines = list(filter(lambda line: onlyHorizontalOrVertical(line), lines))

# Populate the diagram with 0s
for y in range(0, diagramSize + 1):
    row = []
    for x in range(0, diagramSize + 1):
        row.append(0)
    diagram.append(row)

# Populate the diagram with the lines.
for line in lines:
    points = convertToPoints(line)
    for point in points:
        # Reverse the coordinates because y is inverted
        diagram[point.y][point.x] += 1

# Count the number of intersections >= 2
count = 0
for y in range(0, diagramSize):
    for x in range(0, diagramSize):
        if (diagram[x][y] >= 2):
            count += 1

printDiagram()
print(count) 

# for point in points:
#     print(point.printMe())

# for line in lines:
#     print(line.printMe())
# print(lines)