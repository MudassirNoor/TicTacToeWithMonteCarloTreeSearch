from copy import deepcopy

class Board:
    EMPTYCHARACTER = "_"
    BOARDLENGTH = 9
    def __init__(self, currentBoard):
        self.boardArray = deepcopy(currentBoard)

    def display(self):
        for i in range(Board.BOARDLENGTH):
            if i > 0 and i % 3 == 0: print()
            text = str(self.boardArray[i])
            if text is not Board.EMPTYCHARACTER:
                print(text + "\u0332" + "|", end="")
            else:
                print(text + "|", end="")
        print()

    def getLegalPositions(self):
        positionIndexes = list()
        for i in range(Board.BOARDLENGTH):
            if self.boardArray[i] is Board.EMPTYCHARACTER:
                positionIndexes.append(i)
        return positionIndexes

    def checkWin(self, character):
        if self.checkRows(character) is True:
            return True
        elif self.checkColumns(character) is True:
            return True
        elif self.checkDiagonals(character) is True:
            return True
        else:
            return False

    def checkDraw(self, characterA, characterB):
        if Board.EMPTYCHARACTER not in self.boardArray:
            if self.checkWin(characterA) is False and self.checkWin(characterB) is False:
                return True
        return False

    def checkRows(self, character):
        for i in range(0, Board.BOARDLENGTH, 3):
            if self.boardArray[i] == self.boardArray[i + 1] == self.boardArray[i + 2] == character:
                return True
        return False

    def checkColumns(self, character):
        for i in range(3):
            if self.boardArray[i] == self.boardArray[i + 3] == self.boardArray[i + 6] == character:
                return True
        return False

    def checkDiagonals(self, character):
        if self.boardArray[0] == self.boardArray[4] == self.boardArray[8] == character:
            return True
        elif self.boardArray[6] == self.boardArray[4] == self.boardArray[2] == character:
            return True
        else:
            return False

    def updateBoard(self, board):
        self.boardArray = board