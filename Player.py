class Player:
    def __init__(self, playerNum):
        self.character = ""
        self.turn = False
        self.playerNum = playerNum

    def setTurn(self):
        self.turn = True

    def unsetTurn(self):
        self.turn = False

    def setCharacter(self, character):
        self.character = character

    def getPlayerNum(self):
        return self.playerNum
