# Find the intersection of of lines.
fp = open("input2")
lines = fp.readlines()

# Represents a point with an x and y coordinate.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def printMe(self):
        return (self.x + "," + self.y)

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
    return Point(splitPoint[0], splitPoint[1])

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


lines = list(map(convertToLine, lines))
lines = list(filter(lambda line: onlyHorizontalOrVertical(line), lines))

for line in lines:
    print(line.printMe())