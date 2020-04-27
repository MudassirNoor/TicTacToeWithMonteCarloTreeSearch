from Node import Node
from State import State
from MonteCarloTreeSearch import MonteCarloTreeSearch
import Constants

def Game(board, human, computer):
    valid = False
    choice = ""
    if human.turn is True:
        state = State(board, human, computer)
    else:
        state = State(board, computer, human)

    node = Node(state, None)
    while state.checkStatus() is Constants.CONTINUE:
        newBoardArray = board.boardArray
        board.display()
        if computer.turn:
            print("Computer is playing its move. Please exude patience:")
            newBoardArray = MonteCarloTreeSearch(node, Constants.SIMULATIONS).state.board.boardArray
            computer.unsetTurn()
            human.setTurn()
        else:
            print("Your turn!")
            while not valid:
                choice = input("Enter position for your move (1 - 9): ")
                legalMoves = board.getLegalPositions()
                if choice not in "123456789" or choice is '':
                    print("Invalid entry. Try Again")
                elif (int(choice) - 1) not in legalMoves:
                    print("Not a legal move")
                else:
                    valid = True
            newBoardArray[int(choice) - 1] = human.character
            human.unsetTurn()
            computer.setTurn()
            valid = False

        state.updateState(newBoardArray)
        node.resetNode(state)

    board.display()
    if board.checkWin(human.character):
        print("You win!")
    elif board.checkWin(computer.character):
        print("You lose!")
    else:
        print("Game was a draw!")
