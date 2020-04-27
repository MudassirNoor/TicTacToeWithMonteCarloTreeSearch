class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.children = list()
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.visits = 0

    def isRoot(self):
        if self.parent is None:
            return True

    def isLeaf(self):
        if self.children is None or len(self.children) is 0:
            return True

    def incrementWins(self):
        self.wins += 1
        self.visits += 1

    def incrementLosses(self):
        self.losses += 1
        self.visits += 1

    def incrementDraws(self):
        self.draws += 1
        self.visits += 1

    def incrementVisits(self):
        self.visits += 1

    def expandNode(self):
        possibleStates = self.state.getPossibleStates()
        if possibleStates is None:
            self.children = None
            return

        for state in possibleStates:
            self.children.append(Node(state, self))

    def getBestChild(self):
        bestNode = self.children[0]
        lastBestScore = bestNode.getNodeScore()
        for child in self.children:
            score = child.getNodeScore()
            if score > lastBestScore:
                bestNode = child
                lastBestScore = score
            elif score == lastBestScore:
                if child.wins >= bestNode.wins:
                    bestNode = child

        return bestNode

    def getBestChildBasedOnVisits(self):
        bestNode = self.children[0]
        for child in self.children:
            if child.visits >= bestNode.visits:
                bestNode = child

        return bestNode

    def getNodeScore(self):
        return self.wins + self.draws

    def resetNode(self, state):
        self.state = state
        self.parent = None
        self.children = list()
        self.visits = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0