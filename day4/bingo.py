# Basically playing a bingo game!!
fp = open("input2")
line = fp.readline()
drawings = line.split(',')
remainingLines = fp.readlines()
remainingLines = list(filter(lambda x: x != '\n', remainingLines))

# Remove newline character from a string and convert to an integer
def removeNewLine(s):
    s.replace('\n', '')
    return int(s)

# Convert a string of space separated numbers to a list of integers
def stringToRow(s):
    row = s.split(' ')
    row = list(filter(lambda x: x != '', row))
    row = list(map(removeNewLine, row))
    return row

# Convert a list of rows to a bingo card
def createBingoCard(cardString):
    card = []
    for i in range(5):
        card.append(stringToRow(cardString[i]))
    return card

# Create a list of bingo cards from list of rows
def createCards(lines):
    cards = []
    index = 0
    while index < len(lines) - 4:
        cards.append(createBingoCard(lines[index:index+5]))
        index += 5
    return cards

drawings = list(map(removeNewLine, drawings))
bingoCards = createCards(remainingLines)

print(drawings)
print(bingoCards)
