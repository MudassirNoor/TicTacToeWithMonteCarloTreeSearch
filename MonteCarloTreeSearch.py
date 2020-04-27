from random import randrange, seed
from Node import Node
import Constants
import math

#Source: https://www.baeldung.com/java-monte-carlo-tree-search

def MonteCarloTreeSearch(rootNode : Node, SIMULATIONS):
    rootNode.expandNode()
    while SIMULATIONS != 0:
        selectedChild = selectPromisingNode(rootNode)
        result = simulate(selectedChild)
        updateScores(selectedChild, result)
        SIMULATIONS -= 1

    resultNode = rootNode.getBestChildBasedOnVisits()
    return resultNode

# Assuming that the node has already been expanded
def simulate(node : Node):
    seed()
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

def updateScores(node : Node, result : int):
    tempNode = node
    while not tempNode.isRoot():
        if result is Constants.COMPUTER:
            tempNode.incrementWins()
        elif result is Constants.HUMAN:
            tempNode.incrementLosses()
        else:
            tempNode.incrementDraws()
        tempNode = tempNode.parent

    tempNode.incrementVisits()

def selectPromisingNode(parentNode : Node):
    for child in parentNode.children:
        if child.visits == 0:
            return child

    bestUpperConfidenceBound = 0.0
    bestNode = parentNode.children[0]

    for child in parentNode.children:
        upperConfidence = upperConfidenceBound(parentNode.visits, child.getNodeScore(), child.visits)
        if (upperConfidence >= bestUpperConfidenceBound):
            bestNode = child
            bestUpperConfidenceBound = upperConfidence

    return bestNode

def upperConfidenceBound(parentVisits : int, childNodeScore : int, childNodeVisits : int):
    return childNodeScore / childNodeVisits + math.sqrt(2 * math.log(parentVisits) / childNodeVisits)
