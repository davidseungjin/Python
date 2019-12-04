import project4_mechanic_01 as pm

class ColumnGame:
    def __init__(self, user_column, user_row, user_option='EMPTY'):
        self._running = True
        self._matched = False
        self._column = user_column
        self._row = user_row
        self._option = user_option
        self._gameboard = []
        # self._state = spots.SpotsState()

    def getColumn(self) -> int:
        return self._column

    def getRow(self) -> int:
        return self._row

    'I am not sure whether this function "getList" is necessary'
    def getList(self):
        return self._gameboard

    def getBoard(self) -> [[str]]:
        if self._option == 'EMPTY':
            return self._EmptyBoard()
        elif self._option == 'CONTENTS':
            # print('option is CONTENTS')
            return self._ContentsBoard()

    def _setBoard(self, newsetting):
        self._gameboard = newsetting

    def _EmptyBoard(self):
        myboard = []
        for col in range(self._row):
            # print('column in _EmptyBoard')
            myboard.append([])
            for row in range(self._column):
                # print('row in _EmptyBoard')
                myboard[-1].append('   ')
        self._option = 'CONTENTS'
        # print('myboard in EMPTYboard is ', myboard)
        return myboard

    def _ContentsBoard(self):
        if self._gameboard != []:
            # print(' THIS is game board while playing. ')
            return self._gameboard
        return self._InitialBoard()

    def _InitialBoard(self):
        mylist = []
        for n in range(self._row):
            mysublist = []
            myinput = input('input blocks in a row ')
            while len(myinput) != self._column:
                myinput = input('Incorrect width of block. Must be the same width as column width. input again ')
            for i in myinput:
                mysublist.append(i)
            for i in range(len(mysublist)):
                mysublist[i] = ' ' + mysublist[i] + ' '
            mylist.append(mysublist)
        self._setBoard(mylist)
        self._fill_the_hole_recursion()
        return mylist

    def _displayBoard(self):
        self._gameboard = self.getBoard()
        # print('self._gameboard in _displayBoard is ', self._gameboard)           # Later this should be eliminated.
        for space in self._gameboard:
            d = []
            for tile in space:
                d.append(tile)
            print('|' + ''.join(d) + '|')
        print(' ' + '-' * 3 * self.getColumn() + ' ')

    def _fill_the_hole_recursion(self):
        for i in range(self._row-1):
            self._fill_the_hole()
        # self._displayBoard()

    def _fill_the_hole(self):
        display = self._gameboard
        for i in range(self._row -1, -1, -1):
            for j in range(self._column-1, -1, -1):
                # print(i, j, display[i][j])
                if i > 0:
                    try:
                        if display[i][j] == '   ' and display[i-1][j] != '   ':
                            display[i][j] = display[i-1][j]
                            display[i-1][j] = '   '
                    except:
                        continue
        self._setBoard(display)

    def rotateFaller(self, block):
        if block._done != True:
            print('block._faller[0] before = ', block._faller[0])
            print('block._faller[1] before = ', block._faller[1])
            print('block._faller[2] before = ', block._faller[2])
            temp = block._faller[0]
            block._faller[0] = block._faller[1]
            block._faller[1] = block._faller[2]
            block._faller[2] = temp
            print('block._faller[0] after = ', block._faller[0])
            print('block._faller[1] after = ', block._faller[1])
            print('block._faller[2] after = ', block._faller[2])
            i = min(self._row - 1, block._faller_count-1)
            print('i before if statement is ', i)
            display = self._gameboard
            if i == 0:
                # print('i is in startandfalling is ', i)
                display[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            if i == 1:
                display[i - 1][int(block.col) - 1] = '[' + block._faller[1] + ']'
                display[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            if 2 <= i < self._row:
                # print('condition satisfied')
                print('i is ', i)
                for tomakeblank in range(i - 2):
                    display[tomakeblank][int(block.col) - 1] = '   '
                display[i - 2][int(block.col) - 1] = '[' + block._faller[0] + ']'
                display[i - 1][int(block.col) - 1] = '[' + block._faller[1] + ']'
                display[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            self._setBoard(display)

    def _moveLeft(self, block):
        i = min(self._row - 1, block._faller_count-1)
        if (int(block.col) -1) > 0 and block._is_frozen == False:
            print('block._is_frozen is ', block._is_frozen)
            print('i is ', i)
            print('block.col is ', block.col)
            # block._faller_count -= 1
            if i == 0 and self._gameboard[i][int(block.col) - 2] == '   ':
                for n in range(i + 1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) - 1
            if i == 1 \
                    and self._gameboard[i-1][int(block.col) - 2] == '   ' \
                    and self._gameboard[i][int(block.col) - 2] == '   ':
                for n in range(i + 1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) - 1
                print(block.col)
            if 2 <= i < self._row -1\
                    and self._gameboard[i-2][int(block.col) - 2] == '   ' \
                    and self._gameboard[i-1][int(block.col) - 2] == '   ' \
                    and self._gameboard[i][int(block.col) - 2] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col)-1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) - 1

    def _moveRight(self, block):
        i = min(self._row - 1, block._faller_count-1)
        # block._faller_count -= 1
        if (int(block.col) - 1) < (self._column - 1) and block._is_frozen == False:
            print('i in _moveRight is ', i)
            print('block.col is ', block.col)
            if i == 0 and self._gameboard[i][int(block.col)] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) + 1
            if i == 1 \
                    and self._gameboard[i - 1][int(block.col)] == '   ' \
                    and self._gameboard[i][int(block.col)] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) + 1
                print(block.col)
            if 2 <= i < self._row -1 \
                    and self._gameboard[i - 2][int(block.col)] == '   ' \
                    and self._gameboard[i - 1][int(block.col)] == '   ' \
                    and self._gameboard[i][int(block.col)] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) + 1

    def _match(self):
        'Traget and marking only'
        display = self._gameboard
        for i in range(self._row - 1, -1, -1):
            for j in range(self._column - 1, -1, -1):
                # set target, compare horizontal, vertical, diagonal with target and index 1
                # if satisfy, change it between sentinels. *target*
                # print(display)
                target = display[i][j][1]
                # print('target is ', target)
                # print('i, j is %d, %d' % (i, j))
                if target != ' ':
                    # try:
                    #     if display[i-1][j][1] == target and display[i-2][j][1] == target:
                    #         # print('column match case: bottom to top')
                    #         display[i-1][j] = '*' + target + '*'
                    #         display[i-2][j] = '*' + target + '*'
                    #         display[i][j] = '*' + target + '*'
                    #         self._matched = True
                    # except:
                    #     pass
                    try:
                        if display[i+1][j][1] == target and display[i+2][j][1] == target:
                            # print('column match case: top to bottom')
                            display[i+1][j] = '*' + target + '*'
                            display[i+2][j] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
                    # try:
                    #     if display[i][j-1][1] == target and display[i][j-2][1] == target:
                    #         # print('row match case: right to left')
                    #         display[i][j-1] = '*' + target + '*'
                    #         display[i][j-2] = '*' + target + '*'
                    #         display[i][j] = '*' + target + '*'
                    #         self._matched = True
                    # except:
                    #     pass
                    try:
                        if display[i][j+1][1] == target and display[i][j+2][1] == target:
                            # print('row match case: left to right')
                            display[i][j+1] = '*' + target + '*'
                            display[i][j+2] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
                    try:
                        if display[i-1][j-1][1] == target and display[i-2][j-2][1] == target and i >= 2 and j >= 2:
                            # print('Diagonal Match, north west direction')
                            display[i-1][j-1] = '*' + target + '*'
                            display[i-2][j-2] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
                    try:
                        if display[i-1][j+1][1] == target and display[i-2][j+2][1] == target and i >= 2:
                            # print('Diagonal Match, north east direction')
                            display[i-1][j+1] = '*' + target + '*'
                            display[i-2][j+2] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
        # self._displayBoard()
        self._setBoard(display)

    def _eliminate_matched(self):
        'Traget and marking only'
        # myintentionalinput = input()
        display = self._gameboard
        for i in range(self._row - 1, -1, -1):
            for j in range(self._column - 1, -1, -1):
                if display[i][j][0] == '*':
                    display[i][j] = '   '
        self._setBoard(display)
        self._fill_the_hole_recursion()
        self._matched = False
        # self._displayBoard()

    def startandfalling(self, block):
        i = min(self._row - 1, block._faller_count)
        print('block._faller_count is ', block._faller_count)
        print('i is ', i)

        if i == 0 and self._gameboard[i][int(block.col)-1] == '   ':
            # print('i is in startandfalling is ', i)
            self._gameboard[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            block._faller_count += 1
        if i == 1 \
                and self._gameboard[i][int(block.col)-1] == '   ':
            self._gameboard[i-1][int(block.col) - 1] = '[' + block._faller[1] + ']'
            self._gameboard[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            block._faller_count += 1
        if 2 <= i < self._row \
                and self._gameboard[i][int(block.col) - 1] == '   ':
            # print('condition satisfied')
            # print('i is ', i)
            for tomakeblank in range(i-2):
                self._gameboard[tomakeblank][int(block.col) - 1] = '   '
            self._gameboard[i-2][int(block.col) - 1] = '[' + block._faller[0] + ']'
            self._gameboard[i-1][int(block.col) - 1] = '[' + block._faller[1] + ']'
            self._gameboard[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            block._faller_count += 1
        # print('block._faller_count ', block._faller_count)
        # self.landing(block)

    def landing(self, block):
        try:
            # print('block._faller_count is ', block._faller_count)
            if block._faller_count == self._row or self._gameboard[block._faller_count][int(block.col) - 1] != '   ':
                if block._faller_count == 1:
                    self._gameboard[block._faller_count - 1][int(block.col) - 1] = '|' + block._faller[2] + '|'
                if block._faller_count == 2:
                    self._gameboard[block._faller_count - 2][int(block.col) - 1] = '|' + block._faller[1] + '|'
                    self._gameboard[block._faller_count - 1][int(block.col) - 1] = '|' + block._faller[2] + '|'
                if block._faller_count > 2:
                    self._gameboard[block._faller_count - 3][int(block.col) - 1] = '|' + block._faller[0] + '|'
                    self._gameboard[block._faller_count - 2][int(block.col) - 1] = '|' + block._faller[1] + '|'
                    self._gameboard[block._faller_count - 1][int(block.col) - 1] = '|' + block._faller[2] + '|'
                block.addFrozen()
            print('block._is_frozen', block._is_frozen)
        except:
            print('maybe row column index error')

    def _checkBlock(self, block):
        print('block._is_frozen in checkBlock', block._is_frozen)
        print('block._faller_count in checkBlock is ', block._faller_count)
        if block._is_frozen:
            # print('is frozen already')
            self._gameboard[block._faller_count - 3][int(block.col) - 1] = ' ' + block._faller[0] + ' '
            self._gameboard[block._faller_count - 2][int(block.col) - 1] = ' ' + block._faller[1] + ' '
            self._gameboard[block._faller_count - 1][int(block.col) - 1] = ' ' + block._faller[2] + ' '
            block._done = True

    def run(self):
        myinput = ''
        # print('test3')
        self._displayBoard()
        # print('test2')
        myinput = input(' myinput out of run fuction ')
        while (self._running) and (myinput != 'Q'):
            # myinput = input(' myinput in run fuction ')
            self._match()
            if self._matched == True:
                print('this????')
                self._displayBoard()
                mytempinput = input(' temp ')
                self._eliminate_matched()
                self._displayBoard()
            if myinput != '' and myinput != 'Q' and myinput != '<' and myinput != 'R' and myinput != '>':
                block = pm.Faller(myinput[2], myinput[4], myinput[6], myinput[8])
                self.startandfalling(block)
                self._displayBoard()
                while block._done != True:
                    mysubinput = input('  test111   ')
                    if mysubinput =='':
                        self.startandfalling(block)
                        self.landing(block)
                        # print('above displayBoard function of block._done')
                        self._displayBoard()
                        self._checkBlock(block)
                        if block._done == True:
                            mysubinput = input(' test 222   ')
                            self._displayBoard()
                    if mysubinput == 'R':
                        self.rotateFaller(block)
                        # self._displayBoard()
                        # block._faller_count = max(block._faller_count - 1, 0)
                        # self.startandfalling(block)
                        print('block._faller_count is in R function', block._faller_count)
                        self._displayBoard()
                    if mysubinput == '<':
                        self._moveLeft(block)
                        self.startandfalling(block)
                        self._displayBoard()
                    if mysubinput == '>':
                        self._moveRight(block)
                        self.startandfalling(block)
                        self._displayBoard()
                # self._displayBoard()
                print('block._faller_count', block._faller_count)
                print('block._done', block._done)
            try:
                if block._faller_count < 3 and block._done == True:
                    self._running = False
                    print('self._running', self._running)
            except:
                pass
            myinput = input(' myinput in run fuction ')
        print("GAME OVER")


    def _end_game(self) -> bool:
        if block._faller_count >= 3:
            return False
        return True

if __name__ == '__main__':
    user_row = int(input('input row you want '))
    user_column = int(input('input column you want '))
    gamestatus = input('EMPTY or CONTENTS ')

    mygame = ColumnGame(user_column, user_row, gamestatus)
    mygame.run()