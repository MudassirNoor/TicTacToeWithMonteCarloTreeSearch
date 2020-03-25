from random import randrange, seed
from Node import Node
import Constants

def MonteCarloTreeSearch(rootNode):
    rootNode.expandNode()
    for child in rootNode.children:
        sampleSimulations = Constants.SIMULATIONS
        while sampleSimulations != 0:
            result = simulate(child)
            updateScores(child, result)
            sampleSimulations -= 1

    resultNode = rootNode.getBestChild()
    return resultNode

# Assuming that the node has already been expanded
def simulate(node):
    seed()
    node : Node
    status = node.state.checkStatus()
    playNode = node
    while status is Constants.CONTINUE:
        if playNode.isLeaf():
            playNode.expandNode()

        length = len(playNode.children)
        randomNode = playNode.children[randrange(0, length)]
        status = randomNode.state.checkStatus()
        if status is not Constants.CONTINUE:
            return status
        else:
            playNode = randomNode

    return status

def updateScores(node, result):
    tempNode = node
    while not tempNode.isRoot():
        if result is Constants.COMPUTER:
            tempNode.incrementWins()
        elif result is Constants.HUMAN:
            tempNode.incrementLosses()
        else:
            tempNode.incrementDraws()
        tempNode = tempNode.parent
