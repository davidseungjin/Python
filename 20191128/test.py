class Faller:
def __init__(self, col, color1, color2, color3):
self.col = col
self._color1 = color1
self._color2 = color2
self._color3 = color3
self._faller = self._generateFaller()
self.is_frozen = False
self.is_landing = False
self._faller_count = 0
self._bottom_count = 0

def getFaller(self) -> list:
return self._faller

def getCol(self) -> int:
return self.col

def rotateFaller(self):
self._faller = self._faller[-1:] + self._faller[-3:-1]

def _generateFaller(self) -> list:
faller = []
faller.append(self._color1)
faller.append(self._color2)
faller.append(self._color3)
return faller

def addFrozen(self):
self.is_frozen = True

def addLanding(self):
self.is_landing = True


#tick -> ui

class GameBoard:
def __init__(self, row: int, column: int, field: str):
self._row = row
self._column = column
self._field = field
self._board = self.getField()
#match, land


def getRow(self) -> int:
return self._row
def getColumn(self) -> int:
return self._column
def getList(self):
return self._board

def getField(self) -> [[str]]:
if self._field == 'EMPTY':
self._board = self._generateEmptyField()
return self._board
elif self._field == 'CONTENTS':
self._board = self._generateContentField() #wip
return self._board
###
def startFall(self, block):
self._board[0][int(block.col) -1] = '[' + block._faller[2] + ']'
block._bottom_count = 1
block._faller_count = 1

def falling(self, block):
if block._faller_count < self._row:
if block._faller_count > 0:
self._board[block._faller_count][int(block.col) -1] = '[' + block._faller[2] + ']'
self._board[block._faller_count-1][int(block.col) -1] = '[' + block._faller[1] + ']'
if block._faller_count > 1:
self._board[block._faller_count][int(block.col) -1] = '[' + block._faller[2] + ']'
self._board[block._faller_count-1][int(block.col) -1] = '[' + block._faller[1] + ']'
self._board[block._faller_count-2][int(block.col) -1] = '[' + block._faller[0] + ']'
if block._faller_count > 2:
self._board[block._faller_count-3][int(block.col) -1] = ' '
block._faller_count += 1
block._bottom_count += 1
self.landing(block)

def landing(self, block):
'''
block - faller object
self._faller_count - the row # of the lowest jewel
'''
# TODO: Implement check if above jewel
if block._bottom_count == self._row and (self._board[block._bottom_count-1][int(block.col) -1] != ' '):
self._board[block._bottom_count-1][int(block.col) -1] = '|' + block._faller[2] + '|'
self._board[block._bottom_count-2][int(block.col) -1] = '|' + block._faller[1] + '|'
self._board[block._bottom_count-3][int(block.col) -1] = '|' + block._faller[0] + '|'
block.addLanding() ###
return True
return False



def checkBlock(self, block):
self._board[block._bottom_count-1][int(block.col) -1] = ' ' + block._faller[2] + ' '
self._board[block._bottom_count-2][int(block.col) -1] = ' ' + block._faller[1] + ' '
self._board[block._bottom_count-3][int(block.col) -1] = ' ' + block._faller[0] + ' '
block._bottom_count = 0
block.addFrozen()

def updateBlock(self, block):
    if '[' in self._board[block._bottom_count-1][int(block.col) -1]:
        self._board[block._bottom_count-1][int(block.col) -1] = '[' + block._faller[2] + ']'
        self._board[block._bottom_count-2][int(block.col) -1] = '[' + block._faller[1] + ']'
        self._board[block._bottom_count-3][int(block.col) -1] = '[' + block._faller[0] + ']'
    else:
        self._board[block._bottom_count-1][int(block.col) -1] = '|' + block._faller[2] + '|'
        self._board[block._bottom_count-2][int(block.col) -1] = '|' + block._faller[1] + '|'
        self._board[block._bottom_count-3][int(block.col) -1] = '|' + block._faller[0] + '|'

###move right, left, landing, frozen, rotate

###

def _generateEmptyField(self):
    field = []
    for col in range(self._row):
        field.append([])
    for row in range(self._column):
        field[-1].append(' ') #3 spaces
    return field

def _generateContentField(self): #wip
    content = []
    jewel = []
    for col in range(self._row):
        jewel.append(input())
    for color in jewel:
        temp = []
    for t in color:
        slot = ' ' + t + ' '
        temp.append(slot)
        content.append(temp)
    return content


def displayField(game: GameBoard):
    display = game.getList()
    for space in display:
        d = []
        for tile in space:
            d.append(tile)
            print('|' + ''.join(d) + '|')
            print(' ' + '-'*3*game.getColumn() + ' ')


if __name__ == '__main__':
    print('Please enter how many rows.')
    user_row = int(input())
    print('Please enter how many columns.')
    user_column = int(input())
    print('Please enter EMPTY or CONTENTS for the option to fill the field or not.')
    start = input()
    board = GameBoard(user_row, user_column, start)
    displayField(board)
    ####
    while True:
        user_create = input()
        block = Faller(user_create[2], user_create[4], user_create[6], user_create[8])
        print(block)
        count = 0
        board.startFall(block)
        displayField(board)
            while not block.is_frozen:
            u = input()
                if u == "R" and block.is_landing:
                    block.rotateFaller()
                    board.updateBlock(block)
                    displayField(board)
                elif u == 'R' and not block.is_landing:
                    block.rotateFaller()
                    board.updateBlock(block)
                    displayField(board)
                elif u == '' and block.is_landing:
                    board.checkBlock(block)
                    displayField(board)
                else:
                    board.falling(block)
                    displayField(board)
                #if the top one is not in the board yet
                #check last one for < >