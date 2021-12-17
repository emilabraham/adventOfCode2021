# Fold the transparent paper and align the dots
fp = open("input")
lines = fp.readlines()
coordinates = []
folds = []


# Remove newline character from a string
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

print(coordinates)
print(folds)
