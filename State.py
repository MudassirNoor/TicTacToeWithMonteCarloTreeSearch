from Player import Player
from Board import Board
import Constants

class State:
    def __init__(self, board, turnPlayer, otherPlayer):
        turnPlayer : Player
        self.board = board
        self.turnPlayer = turnPlayer
        self.otherPlayer = otherPlayer

    # GetPossibleStates must be called after checking state status
    def getPossibleStates(self):
        possiblePositions = self.board.getLegalPositions()
        if len(possiblePositions) == 0:
            return None

        newStates = list()
        for position in possiblePositions:
            newStates.append(State(self.getNewBoard(position), self.otherPlayer, self.turnPlayer))

        return newStates

    # To be internally used by getPossible states to get new game boards
    def getNewBoard(self, position):
        board = Board(self.board.boardArray)
        board.boardArray[position] = self.turnPlayer.character
        return board

    # Should be checked first
    def checkStatus(self):
        isDraw = self.board.checkDraw(self.turnPlayer.character, self.otherPlayer.character)
        hasOtherPlayerWon = self.board.checkWin(self.otherPlayer.character)
        hasTurnPlayerWon = self.board.checkWin(self.turnPlayer.character)

        if isDraw:
            return Constants.DRAW
        elif hasOtherPlayerWon :
            return self.otherPlayer.getPlayerNum()
        elif hasTurnPlayerWon:
            return self.turnPlayer.getPlayerNum()
        else:
            return Constants.CONTINUE

    def updateState(self, boardArray):
        self.board.updateBoard(boardArray)
        tempPlayer = self.turnPlayer
        self.turnPlayer = self.otherPlayer
        self.otherPlayer = tempPlayer
