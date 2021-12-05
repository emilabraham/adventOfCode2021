# Basically playing a bingo game!!
fp = open("input")
line = fp.readline()
drawings = line.split(',')
remainingLines = fp.readlines()
remainingLines = list(filter(lambda x: x != '\n', remainingLines))

# Represents a bingo slot.
# The value represents the number that is in the slot.
# The drawn indicates whether the number has been drawn.
class BingoValue:
    def __init__(self, value, drawn):
        self.value = value
        self.drawn = drawn

    # Return a string version of the bingo value.
    def printMe(self):
        isDrawn = "F"
        if (self.drawn):
            isDrawn = "T"
        return str(self.value) + ":" + isDrawn

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

# Print a single bingo card
def printCard(card):
    for row in card:
        for value in row:
            s = value.printMe()
            print(s, end=' ')
        print("\n")
    print("---------------------------------")

# Print a list of bingo cards
def printCards(cards):
    for card in cards:
        printCard(card)

# Mark down the number in the bingo card. Return the card
def drawNumber(card, number):
    for row in card:
        for value in row:
            if (value.value == number):
                value.drawn = True
    return card

# Return True if all the values in the row are drawn
def validateRow(row):
    rowWin = True
    for value in row:
        if (value.drawn == False):
            rowWin = False
    return rowWin

# Return false if there is no bingo in the card.
# Return the row or column that has a bingo
def validateCard(card):
    rowWin = False
    for row in card:
        if validateRow(row) == True:
            rowWin = list(map(lambda x: x.value, row))
            break

    if (rowWin != False):
        return rowWin

    columnWin = False
    for column in range(5):
        columns = []
        for row in card:
            columns.append(row[column])
        if validateRow(columns) == True:
            columnWin = list(map(lambda x: x.value, columns))
            break
    if (columnWin != False):
        return columnWin
    return False

# Return the sum of the unmarked numbers in the card
def sumUnMarked(card):
    sum = 0
    for row in card:
        for value in row:
            if (value.drawn == False):
                sum += value.value
    return sum

# Validate the cards. Return the winning numbers or False
def validateCards(cards):
    for card in cards:
        validation = validateCard(card)
        if (validation != False):
            return sumUnMarked(card)
    return False

# Draw from a list of numbers and mark them on the cards
def drawNumbers(cards, numbers):
    for draw in numbers:
        list(map(lambda x: drawNumber(x, draw), cards))
        # Will either be a sum the winning numbers or False
        validation = validateCards(cards)
        if validation != False:
            printCards(cards)
            print(validation * draw)
            break

drawings = list(map(removeNewLine, drawings))
bingoCards = createCards(remainingLines)
bingoCards = list(map(lambda card: list(map(lambda row: list(map(lambda y: BingoValue(y, False), row)), card)), bingoCards))
drawNumbers(bingoCards, drawings)
